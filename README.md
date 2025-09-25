# Szakdolgozat 2.0 – Sprint 1 Kickoff

Ez a repository a "Szakdolgozat 2.0: Bevezetés a Modern, MI-Vezérelt Szoftverfejlesztésbe" kurzus GitHub Classroom sablonja. A cél, hogy az első sprint végére egy validált problémaleírással és a hozzá tartozó kutatási artefaktumokkal rendelkezz.

## Tartalom
- `course.yaml`: hallgatói metaadatok és track választás
- `prd.yaml`: a Product Requirements Document első verziója
- `ai/`: az MI-eszközök használatának terve és naplója
- `interviews/`: legalább öt felhasználói interjú jegyzőkönyve JSON formátumban
- `market/competitors.csv`: három vagy több versenytárs elemzése táblázatos formában
- `architecture/adr/`: Architecture Decision Record(ok) a kulcsdöntésekről
- `scripts/validate.py`: helyi validátor a sprint leadása előtt
- `sprints/01/`: sprint-specifikus segédanyagok és státusz

## Sprint 1 Követelmények
1. Probléma, célcsoport és értékajánlat pontos összegyűjtése a `prd.yaml`-ban.
2. Minimum öt interjú lebonyolítása és dokumentálása az `interviews/` mappában.
3. Minimum három versenytárs analizálása a `market/competitors.csv` fájlban.
4. Legalább egy ADR rögzítése az első technológiai döntésről.
5. MI-használati terv és napló vezetése az `ai/` mappában.
6. A `scripts/validate.py --sprint 1` sikeres futása a leadás előtt.

## Használat
```bash
python scripts/validate.py --sprint 1
```
A szkript ellenőrzi a sprint specifikus fájlok létét és formátumát, valamint összeveti az AI napló bejegyzéseinek számát a `course.yaml` elvárásával.

## License
MIT
