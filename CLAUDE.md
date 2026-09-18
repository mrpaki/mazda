# East Auto Servis (eastservis.rs): kontekst projekta

Redizajn sajta za EAST Auto Servis, specijalizovani Mazda servis u Beogradu.
Statički sajt, custom HTML/CSS/JS, bez frameworka i bez build alata osim jedne Python skripte.
Dizajn je završen i odobren. NE MENJAJ DIZAJN osim ako to eksplicitno ne tražim.

## Struktura

- `build.py`: JEDINI IZVOR ISTINE za sadržaj. Generiše svih 7 HTML strana sa zajedničkim headerom i footerom.
- `index.html`, `servis.html`, `modeli.html`, `sertifikati.html`, `galerija.html`, `o-nama.html`, `kontakt.html`: GENERISANI fajlovi. Ne edituj ih ručno.
- `css/style.css`: jedan stylesheet za ceo sajt.
- `js/main.js`: sav JS (vanilla, bez biblioteka).
- `video/`: ovde ide `hero.mp4`, trenutno ne postoji.

Tok rada: izmena u `build.py` (sadržaj/HTML) ili u `css`/`js` → `python3 build.py` → provera u browseru.

## Dizajn sistem (ne dirati)

- Boje (CSS varijable u `:root`):
  - `--ink #18202C` (grafitno plava, header i tamne sekcije)
  - `--ink-2 #222C3B` (footer)
  - `--paper #EDF0F3` (svetle sekcije)
  - `--steel #5E6877` (sekundarni tekst)
  - `--line #D3D9E0`
  - `--red #A3162A` (Mazda crvena, SAMO za CTA dugmad i akcente)
- Font: Archivo (Google Fonts, varijabilna širina). Naslovi idu sa `font-stretch:125%`, tekst je normalne širine. Nema drugih fontova.
- Potpisni element: "obrtomer" u hero sekciji naslovne. Skala 0–8 ×1000 o/min sa crvenom zonom od 6.5 naviše i jednom animacijom "dizanja gasa" na učitavanju. To je JEDINA automatska animacija na sajtu. Ne dodavati fade-in, slide-up i slične efekte.
- Unutrašnje strane imaju tamni `.page-head` sa tankom linijom na dnu: poslednjih 18.75% je crveno, kao crvena zona obrtomera.
- Radius 4px, bez senki na karticama, bez gradijenata kao dekoracije.
- Tekst: srpski latinica, sentence case, bez ALL CAPS labela, bez "→" u linkovima.
- Pristupačnost je već urađena i treba da ostane: skip link, `:focus-visible`, `aria` na meniju/lightbox-u/filterima, `prefers-reduced-motion`, semantički HTML.

## Naslovna, redom sekcija

1. Hero: pozadinska fotografija i opcioni video, naslov "Servis za vašu Mazdu.", CTA dugmad, obrtomer, 3 činjenice (od 2000, 1500+ klijenata, 15 sertifikata).
2. "Jedna marka, šesnaest godina iskustva."
3. "Šta radimo": 4 usluge.
4. "Kako izgleda servis kod nas": 5 numerisanih koraka.
5. "Modeli koje servisiramo": tamna sekcija sa "zidom" naziva modela.
6. "Naš servisni tim": 4 placeholdera, podaci su u listi `TEAM` u `build.py`.
7. "Iz radionice": 5 fotografija, link ka galeriji.
8. Kontakt blok: veliki broj telefona, mejl, radno vreme, adresa, mapa.

## Podaci o servisu (tačni, potvrđeni)

- Telefon: 064 144 63 43 (`+381641446343`)
- Mejl: office@eastservis.rs
- Adresa: Slanački put 123a, Višnjička Banja, Beograd
- Radno vreme: pon–pet 08–17 h; subota i nedelja NE RADI
- Facebook: https://www.facebook.com/eastautoservis
- Otvoren 2000 (26 godina iskustva), proširen 2012, 1500+ klijenata, 15 Mazda sertifikata
- Radi ISKLJUČIVO Mazda vozila. Nikakve druge marke (Kia, Hyundai, Toyota su namerno izbačene).

## Strana Modeli (dogovoreno)

- Aktuelni: Mazda 2, 3, 6, CX-3, CX-30, CX-5, CX-60, MX-30, MX-5
- Prethodne generacije: Mazda 5, CX-7, Mazda 3 MPS, Mazda 6 MPS
- Wankel motori: RX-7, RX-8 (posebna grupa)
- Stariji modeli (121, 323, 323F, 626, 929, Xedos 6/9, MX-3, MX-6, Premacy, MPV, Demio) se rade SAMO uz prethodni dogovor, sa tekstom "rado ćemo pogledati i vašeg „dedu“".
- Tribute i BT-50 NE idu na sajt.
- Pojedinačne strane modela: naziv → "Servis za [model]" (manji font) → manja slika/dijagram → uvodni tekst → "Generacije koje servisiramo" → "Na šta obraćamo pažnju" (nacrt, klijent potvrđuje) → CTA. Model dobija link (na naslovnoj i strani Modeli) kad se doda u `MODEL_PAGES`. Slike modela u `img/modeli/` (dijagrami/blueprint) ili `img/galerija/` (foto sa zatamnjenom tablicom).

## Funkcionalnosti (urađeno, u main.js)

- Sticky header sa senkom na skrol, mobilni meni (Esc zatvara).
- Lightbox (`<dialog>`) za galeriju i sertifikate: strelice, tastatura, zatvaranje klikom van slike.
- Filter galerije po kategoriji (radionica, Mazda 2, 3, 6, CX, MX-5) sa brojačem.
- Hero video: `video/hero.webm` (VP9) + `video/hero.mp4` fallback, `autoplay muted loop`; ako oba izvora zakažu ili je uključen reduced motion, ostaje poster slika. Dugme "Zvuk" (gore desno) otključava zvuk motora. Obrtomer prati obrte motora iz snimljenog audio envelope-a (`js/hero-rev.js`), sinhronizovano sa `video.currentTime`.
- Forma za zakazivanje na strani Kontakt: validacija imena i telefona, zatim otvara `mailto:` sa popunjenom porukom. Za sada nema backend.
- Mobilna fiksna traka na dnu ekrana ("Pozovite" i "Zakažite") ispod 700px.
- JSON-LD `AutoRepair` na naslovnoj (adresa, geo, radno vreme, telefon).
- Potpis izrade u footeru: ilustracija Mazde (`img/credit-mazda.png`, bela na providnom, 320×120, prikaz 160×60; rezerva za svetle pozadine `img/credit-mazda-tamna.png` u boji #18202C) je dugme — na klik auto "odlazi" ulevo van ekrana i otkriva tekst "Izrada sajta i tehničko održavanje Rondo" sa linkom na rondo.rs. Dozvoljen izuzetak od pravila "jedina animacija je obrtomer" jer se pokreće samo na korisnikov klik; poštuje `prefers-reduced-motion` (tada auto samo nestane).

## Pravila za dalji rad

- Pre svake izmene reci šta planiraš. Ne refaktoriši ono što nije traženo.
- Sadržaj menjaj u `build.py`, nikad direktno u generisanim HTML fajlovima.
- Posle izmene pokreni `python3 build.py` i proveri desktop (1440px) i mobilni (390px) prikaz.
- Nove komponente moraju koristiti postojeće CSS varijable i klase (`.section`, `.section-paper`, `.section-ink`, `.section-head`, `.h2`, `.h3`, `.btn-red`, `.btn-line`, `.link`).
