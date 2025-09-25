# 0001: Kezdeti technológiai stack kiválasztása

- Dátum: 2025-02-09
- Státusz: Elfogadva

## Kontextus
A ResearchFlow MVP-nek gyorsan kell iterálnia a felhasználói visszajelzések alapján. Olyan keretrendszerre van szükség, amelyet a csapat ismer, rendelkezik kész komponenskészlettel, és egyszerűen telepíthető felhőalapú platformokra. A backendhez megbízható relációs adatbázis és tipizált API szükséges.

## Döntés
A frontendhez **Next.js (React)** keretrendszert választunk TypeScript támogatással. A backend szolgáltatás **Node.js (Express)** köré épül, az adatokat pedig **PostgreSQL** tárolja. A fejlesztők jól ismerik a JavaScript/TypeScript ökoszisztémát, így lerövidül az onboarding és gyorsabb a prototípuskészítés.

## Megfontolt alternatívák
- **Vue 3 + Vite + Supabase**: alacsony belépési küszöb és Supabase beépített auth modult ad, de a csapatnak nincs benne gyakorlata.
- **Django + React**: erős admin felületet adna, de két külön build pipeline-t igényel, ami lassítja az MVP fejlesztést.
- **Flutter Web + Firebase**: gyors UI prototípusok, viszont a webböngészős Flutter teljesítményével kapcsolatban még vannak kérdőjelek.

## Következmények
- A TypeScript használatával jobb típusbiztonság érhető el, ami a későbbi refaktorokat támogatja.
- A választott stack jól integrálható Vercel és Railway telepítési környezettel, így a zárt béta előtt is gyorsan publikálható.
- A JavaScript stack magas ökoszisztéma zajt hoz (sok csomag), ezért szükség lesz rendszeres dependency auditokra a Sprint 5-ben.
