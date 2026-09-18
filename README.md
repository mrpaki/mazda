# EAST Auto Servis — sajt

Statični sajt za EAST Auto Servis, specijalizovani Mazda servis u Beogradu.
Privremeni preview (GitHub Pages).

## Struktura

- `build.py` — jedini izvor istine za sadržaj; generiše sve HTML strane sa zajedničkim headerom i footerom.
- `*.html` — generisani fajlovi (ne editovati ručno).
- `css/style.css` — jedan stylesheet.
- `js/main.js` — sav JS (vanilla). `js/hero-rev.js` — envelope obrtaja motora za hero obrtomer.
- `img/` — slike (modeli, logoi delova, galerija). Deo galerije se još hotlinkuje sa eastservis.rs.
- `video/` — `hero.webm` / `hero.mp4` (Mazda MX-5 hero, sa zvukom).

## Build

```bash
python3 build.py
```

## Napomena

Preview je privremen. Deo slika se učitava sa živog sajta eastservis.rs dok se lokalni `img/` ne dopuni.
