# ADR 0001 – Deployment cél választása 

**Dátum:** 2025-10-28  
**Státusz:** Elfogadva

## Kontextus
Preview/hosting megoldás kell alacsony költséggel, gyors build-del, és egyszerű integrációval a CI-hoz.

## Döntés
Választás: Vercel (vagy Netlify/Firebase Hosting). Indoklás: gyors preview link, egyszerű konfiguráció, ingyenes szint.

## Alternatívák
- Firebase Hosting: egyszerű, de CI-integrációhoz külön lépések kellenek.
- VM szolgáltatás: nagyobb kontroll, de több üzemeltetési teher.

## Következmények
- Pozitív: gyors publikálás, stabil preview linkek.
- Negatív: vendor lock-in kockázat, később migrációs költség.
