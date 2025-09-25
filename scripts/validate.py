#!/usr/bin/env python3
"""Egyszerű helyi validátor a Sprint 1 leadandóihoz."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover
    print("[HIBA] A PyYAML csomag nem érhető el. Telepítés: pip install pyyaml", file=sys.stderr)
    raise

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_yaml(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}
    except FileNotFoundError as exc:
        raise ValueError(f"Hiányzó fájl: {path}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"Hibás YAML formátum: {path}\n{exc}") from exc


def validate_course(course_path: Path) -> int:
    data = load_yaml(course_path)
    if not isinstance(data, dict):
        raise ValueError("course.yaml tartalma nem objektum.")

    missing = []
    student = data.get("student")
    if not isinstance(student, dict):
        missing.append("student blokknak objektumnak kell lennie")
    else:
        for key in ("name", "id"):
            if not student.get(key):
                missing.append(f"student.{key} hiányzik vagy üres")

    project = data.get("project")
    if not isinstance(project, dict):
        missing.append("project blokknak objektumnak kell lennie")
    else:
        if not project.get("title"):
            missing.append("project.title hiányzik")
        if "product_ml_features" not in project:
            missing.append("project.product_ml_features hiányzik")

    ai = data.get("ai")
    if not isinstance(ai, dict):
        missing.append("ai blokknak objektumnak kell lennie")
        log_min = 3
    else:
        log_min = ai.get("log_min_entries_per_sprint", 3)
        if not isinstance(log_min, int) or log_min < 0:
            missing.append("ai.log_min_entries_per_sprint egész szám kell legyen")

    if missing:
        raise ValueError("course.yaml ellenőrzési hiba: " + "; ".join(missing))

    return int(log_min)


def validate_prd(prd_path: Path) -> None:
    data = load_yaml(prd_path)
    if not isinstance(data, dict):
        raise ValueError("prd.yaml tartalma nem objektum.")

    def ensure(path: list[str]) -> None:
        cursor = data
        for key in path:
            if not isinstance(cursor, dict) or key not in cursor:
                raise ValueError(f"prd.yaml hiányzó mező: {'/'.join(path)}")
            cursor = cursor[key]
        if isinstance(cursor, (str, list)) and not cursor:
            raise ValueError(f"prd.yaml üres mező: {'/'.join(path)}")

    ensure(["problem", "statement"])
    ensure(["target_audience", "personas"])
    ensure(["value_proposition", "concise"])
    ensure(["scope", "in"])
    ensure(["scope", "out"])
    ensure(["first_tech_decision_ref"])

    ref = data["first_tech_decision_ref"]
    ref_path = REPO_ROOT / ref
    if not ref_path.exists():
        raise ValueError(f"A hivatkozott ADR fájl nem található: {ref}")


def validate_ai_usage(plan_path: Path) -> None:
    load_yaml(plan_path)


def validate_ai_log(log_path: Path, min_entries: int) -> None:
    if not log_path.exists():
        raise ValueError("Hiányzó AI napló: ai/ai_log.jsonl")

    entries = []
    with log_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Érvénytelen JSON az AI naplóban (sor {line_no}): {exc}") from exc
            for key in ("date", "tool", "task", "decision", "notes"):
                if key not in record or not record[key]:
                    raise ValueError(f"AI napló hiányzó mező (sor {line_no}): {key}")
            entries.append(record)

    if len(entries) < min_entries:
        raise ValueError(
            f"Az AI naplóban csak {len(entries)} bejegyzés található, a minimum elvárás {min_entries}."
        )


def validate_interviews(directory: Path) -> None:
    files = sorted(directory.glob("*.json"))
    if len(files) < 5:
        raise ValueError(f"Legalább 5 interjú fájl szükséges, jelenleg {len(files)} található.")

    for path in files:
        with path.open("r", encoding="utf-8") as handle:
            try:
                data = json.load(handle)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Érvénytelen JSON az interjú fájlban: {path}\n{exc}") from exc
        required_keys = {"id", "date", "method", "participant", "consent", "insights", "pain_points"}
        if missing := required_keys - data.keys():
            raise ValueError(f"Interjú fájl hiányzó mezők ({path}): {', '.join(sorted(missing))}")
        if not isinstance(data["participant"], dict):
            raise ValueError(f"participant mezőnek objektumnak kell lennie: {path}")
        for key in ("pseudonym", "segment"):
            if not data["participant"].get(key):
                raise ValueError(f"participant.{key} hiányzik: {path}")
        for key in ("insights", "pain_points"):
            value = data[key]
            if not isinstance(value, list) or not value:
                raise ValueError(f"{key} mező üres vagy nem lista: {path}")


def validate_competitors(csv_path: Path) -> None:
    if not csv_path.exists():
        raise ValueError("Hiányzó market/competitors.csv fájl")

    with csv_path.open("r", encoding="utf-8") as handle:
        reader = list(csv.reader(handle))
    if len(reader) <= 1:
        raise ValueError("A versenytárs CSV-nek legalább három adat sort kell tartalmaznia.")
    headers = reader[0]
    expected = ["name", "url", "pricing_model", "key_strengths", "key_weaknesses"]
    if headers != expected:
        raise ValueError("A versenytárs CSV fejlécének meg kell egyeznie az elvárt struktúrával.")
    if len(reader) - 1 < 3:
        raise ValueError("A versenytárs CSV-ben legalább három versenytárs legyen.")


def validate_adr(directory: Path) -> None:
    files = list(directory.glob("*.md"))
    if not files:
        raise ValueError("Legalább egy ADR markdown fájlnak lennie kell az architecture/adr könyvtárban.")


def validate_sprint_one() -> None:
    min_entries = validate_course(REPO_ROOT / "course.yaml")
    validate_prd(REPO_ROOT / "prd.yaml")
    validate_ai_usage(REPO_ROOT / "ai" / "usage_plan.yaml")
    validate_ai_log(REPO_ROOT / "ai" / "ai_log.jsonl", min_entries)
    validate_interviews(REPO_ROOT / "interviews")
    validate_competitors(REPO_ROOT / "market" / "competitors.csv")
    validate_adr(REPO_ROOT / "architecture" / "adr")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sprint leadási ellenőrző eszköz")
    parser.add_argument("--sprint", required=True, help="Sprint sorszáma, pl. 1")
    args = parser.parse_args()

    if args.sprint != "1":
        print(f"Sprint {args.sprint} ellenőrzése még nincs implementálva.")
        sys.exit(0)

    try:
        validate_sprint_one()
    except ValueError as exc:
        print(f"[FAIL] {exc}")
        sys.exit(1)

    print("[PASS] A Sprint 1 kötelező artefaktumai rendben vannak.")


if __name__ == "__main__":
    main()
