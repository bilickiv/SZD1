# Review folyamat és sablon

Ez a dokumentum rögzíti a Sprint 1 → Sprint 2 átadás során alkalmazott review folyamatot, a sablont és a technikai eszközöket.

## Futtatás (LLM értékelés generálása)

- Környezeti változó: `OPENROUTER_API_KEY` (ne kerüljön verziókezelésbe; lásd `.env.example`).
- Ajánlott modell: `google/gemini-2.5-pro` (OpenRouter). Kimeneti limit: `max_tokens = 60000`.
- Példa parancsok:
  - LLM‑értékelés (részletes, levél stílus):
    - `python3 validate_sprint.py --student 1-sprint-dominikrose887 --output "hallgatok/Rózsa Dominik/sprint1_artifacts.md" --review-output "hallgatok/Rózsa Dominik/review.txt"`
    - vagy csak review generálása: `python3 validate_sprint.py --student 1-sprint-dominikrose887 --output "hallgatok/Rózsa Dominik/review.txt"`
  - vagy a többhallgatós futtató: `bash scripts/run_all.sh`

A script a repóban lévő Sprint 1 artefaktumokból állít össze kontextust, majd a fenti modellel elkészíti a részletes, Sprint 2-re fókuszáló értékelést (`sprint1_artifacts.md`).

## Review stílus és sablon (review.txt)

Minden hallgató review-ja levél stílusú, bővebb bevezetővel induljon (megszólítás, köszönet, téma megnevezése), majd jöhet a részletes bontás. Sablon és minta: `reviews/template.md:1`.

Ajánlott szerkezet:
1) Levél stílusú bevezetés (2–4 bekezdés).
2) Sprint 1 fókusz (DoD) – rövid bulletlista a Sprint 1 elvárt köreiről.
3) Sprint 2 fókusz – javasolt MVP vertikális szelet és indoklás.
4) A 11 leadandó sorrendben, mindegyiknél két blokk:
   - „Sprint 1 állapot” – konkrét, fájlokra hivatkozó megfigyelés.
   - „Sprint 2 fókusz” – hallgatóra szabott következő lépések (példákkal, fájlútvonalakkal, parancsokkal).
5) „Sprint 2 prioritások” – max 3 tétel, de rövid indoklással.
6) „Known issues / Next steps”.
7) Záró, bátorító bekezdés.

Fairness / scope elv:
- Sprint 1-ben nem elvárt leadandók (kód, tesztek/coverage, CI, smoke/preview, IaC/terraform, traceability) hiányát NE tekintsük hibának. Ezeket „Sprint 1 állapot: Sprint 1-ben nem elvárt leadandó; hiánya nem probléma.” megfogalmazással jelezzük, és a „Sprint 2 fókusz”-ban írjuk le a teendőket.
- Valódi hiányosságként csak a Sprint 1 DoD szerinti elemeket jelöljük (PRD, interjúk, market, legalább 1 ADR, AI usage plan/log, repo szerkezet, stb.).

A review a `hallgatok/<név vagy slug>/review.txt` útvonalra kerüljön. Minták:
- `hallgatok/Rózsa Dominik/review.txt:1`
- `hallgatok/Kálmán Ádám/review.txt:1`

## Sprint 2 DoD (hivatkozandó checklist)

- Spec v0.2, konzisztens a kutatással
- 5 user story + AC (INVEST), top 1–2 automatizált acceptance teszt
- ≥5 teszt, coverage ≥60% (JUnit/Cobertura vagy ekvivalens)
- Smoke/preview cél és zöld smoke CI-ben
- MVP E2E flow (screenshot/GIF bizonyítékkal)
- IaC jelen, `terraform validate/plan` mentett artefaktként
- Traceability tábla (Story → AC → Test → Code → CI)
- AI log frissítve konkrét döntésekkel
- Wireframe-ek az MVP-hez (empty/error/success)
- PR + CI zöld, linkek az artefaktokra

## PR review leadás (GitHub Classroom)

- Cím formátum: „Sprint 1 → Sprint 2 review – <Hallgató>”.
- A kommentbe illeszd be a `review.txt` tartalmát.
- Állapot: „Request changes” (mindenkinél vannak korrekciók).
- Linkeld a `hallgatok/<Név>/sprint1_artifacts.md` fájlt a részletes LLM válasz megtekintéséhez.

## Mappanév konvenció

A jelenlegi mappák ékezetes nevei megtarthatók, de a CI/OS kompatibilitás érdekében javasolt a slug-os elnevezésre váltás (pl. `hallgatok/rozsa-dominik/`). Átálláskor a linkeket frissíteni kell.

## Traceability és wireframe formátum

- Traceability: Markdown táblázat (Story → AC → Teszt → Modul → CI lépés).
- Wireframe: PNG/JPG a `wireframes/` mappában (pl. `wireframes/weekly-feed.png`).
