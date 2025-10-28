# ADR 0002 – IaC stratégia 

**Dátum:** 2025-10-28  
**Státusz:** Elfogadva

## Kontextus
Preview környezet tervrajzát szeretnénk kód formában rögzíteni (nem kötelező apply), olcsón, ismételhetően.

## Döntés
Terraform használata validate + plan szintig. Az apply későbbi sprintben történik.

## Alternatívák
- Pulumi: erős nyelvi integráció, de más tanulási görbe.
- Kézi provisioning: gyors indulás, de nincs visszajátszhatóság.

## Következmények
- Pozitív: deklaratív, átlátható infra leírás; plan artefakt auditálható.
- Negatív: kezdeti tanulási igény; modulstruktúra később finomítandó.
