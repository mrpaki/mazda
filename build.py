#!/usr/bin/env python3
"""Generiše statičke HTML strane za eastservis.rs (zajednički header/footer).
Slike se trenutno učitavaju sa postojećeg sajta (IMG). Kada se folder img/
prekopira u projekat, promeniti IMG u "img/" i ponovo pokrenuti: python3 build.py
"""
import os

IMG = "https://eastservis.rs/img/"
# Apsolutna baza za og:image / deljenje na mrežama. PROMENITI na https://eastservis.rs u produkciji.
BASE_URL = "https://mrpaki.github.io/mazda"
PHONE = "+381641446343"
PHONE_TXT = "064 144 63 43"
EMAIL = "office@eastservis.rs"
FB = "https://www.facebook.com/eastautoservis"
MAP = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2830.421125364123!2d20.540623215535767"
       "!3d44.81298467909866!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x475a7a3ecfc94c91%3A"
       "0x3dd3f6d00bd5e0ab!2sMazda+Servis%22East+Auto+Servis%22!5e0!3m2!1ssr!2srs!4v1486586850562")
ADDRESS = "Slanački put 123a, Višnjička Banja, Beograd"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Slana%C4%8Dki+put+123a+Beograd"

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'
ICON_SOUND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4z"/><path class="snd-off" d="M22 9l-6 6M16 9l6 6"/><path class="snd-on" d="M15.5 8.5a5 5 0 0 1 0 7M19 5a9 9 0 0 1 0 14"/></svg>'

PAGES = [
    ("index.html", "Naslovna"),
    ("servis.html", "Servis i delovi"),
    ("modeli.html", "Modeli"),
    ("sertifikati.html", "Sertifikati"),
    ("galerija.html", "Galerija"),
    ("o-nama.html", "O nama"),
    ("kontakt.html", "Kontakt"),
]


def head(title, desc, current, extra=""):
    nav = "\n".join(
        f'        <li><a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{n}</a></li>'
        for f, n in PAGES)
    return f"""<!doctype html>
<html lang="sr-Latn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sr_RS">
<meta property="og:image" content="{BASE_URL}/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Mazda CX-5 na dizalici u servisu EAST Auto Servis">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL}/img/og-image.jpg">
<meta name="theme-color" content="#18202C">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='4' fill='%2318202C'/%3E%3Cpath d='M9 8h14v3.5H13v3h9v3.5h-9v3h10V24H9z' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{extra}</head>
<body>
<a class="skip" href="#main">Preskoči na sadržaj</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="EAST Auto Servis, naslovna">
      <span class="brand-name">EAST</span>
      <span class="brand-sub">Mazda servis Beograd</span>
    </a>
    <nav class="nav" id="nav" aria-label="Glavni meni">
      <ul>
{nav}
      </ul>
    </nav>
    <a class="header-call" href="tel:{PHONE}">{ICON_PHONE}{PHONE_TXT}</a>
    <button class="nav-toggle" aria-controls="nav" aria-expanded="false" aria-label="Otvori meni">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>
<main id="main">
"""


def page_head(h1, lead):
    return f"""<section class="page-head">
  <div class="wrap">
    <h1 class="h1">{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


CTA = f"""<section class="section section-paper">
  <div class="wrap cta-strip">
    <h2 class="h2">Zakažite servis ili pregled pre kupovine</h2>
    <div class="actions">
      <a class="btn btn-red" href="tel:{PHONE}">{ICON_PHONE}Pozovite {PHONE_TXT}</a>
      <a class="btn btn-line" href="kontakt.html">{ICON_CAL}Zakažite online</a>
    </div>
  </div>
</section>
"""

LIGHTBOX = """<dialog class="lightbox" id="lightbox" aria-label="Pregled fotografije">
  <div class="lb-top"><span class="lb-pos"></span>
    <button class="lb-btn lb-close" aria-label="Zatvori"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  </div>
  <div class="lb-stage"><img alt=""></div>
  <p class="lb-caption"></p>
  <button class="lb-btn lb-prev" aria-label="Prethodna"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button>
  <button class="lb-btn lb-next" aria-label="Sledeća"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></button>
</dialog>
"""


def foot(lightbox=False):
    links = "\n".join(f'          <li><a href="{f}">{n}</a></li>' for f, n in PAGES)
    return f"""</main>
{LIGHTBOX if lightbox else ""}<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html"><span class="brand-name">EAST</span><span class="brand-sub">Mazda servis Beograd</span></a>
        <p>Specijalizovani servis za Mazda vozila od 2010. godine. Redovno održavanje, dijagnostika i remont.</p>
      </div>
      <div>
        <h2>Stranice</h2>
        <ul>
{links}
        </ul>
      </div>
      <div>
        <h2>Kontakt</h2>
        <ul>
          <li><a href="tel:{PHONE}">{PHONE_TXT}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{MAP_LINK}" target="_blank" rel="noopener">Slanački put 123a<br>Višnjička Banja, Beograd</a></li>
          <li>Pon–pet 08–17 h</li>
          <li><a href="{FB}" rel="noopener" target="_blank">Facebook stranica</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> EAST Auto Servis, Beograd</span>
      <div class="credit">
        <span class="credit-text" id="credit-text">Izrada sajta i tehničko održavanje <a href="https://rondo.rs" rel="noopener" target="_blank">Rondo</a></span>
        <button class="credit-car" type="button" aria-controls="credit-text" aria-expanded="false" title="Ko je napravio sajt?">
          <img src="img/credit-mazda.png" width="130" height="49" alt="Ko je napravio sajt? Kliknite na auto">
        </button>
      </div>
    </div>
  </div>
</footer>
<nav class="callbar" aria-label="Brzi kontakt">
  <a href="tel:{PHONE}">{ICON_PHONE}Pozovite</a>
  <a href="kontakt.html">{ICON_CAL}Zakažite</a>
</nav>
<script src="js/main.js" defer></script>
</body>
</html>
"""


# ---------------- Podaci ----------------
GALLERY = [
    ("Servis_mazde.jpg", "radionica", "Mazda CX-7, Mazda 5 i Mazda 6 u radionici"),
    ("Servis_mazda_dijagnostika_01.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_02.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_03.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_04.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_05.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_06.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_07.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_08.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_09.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mazda_dijagnostika_10.jpg", "radionica", "Dijagnostika u radionici"),
    ("Servis_mx5.jpg", "mx5", "Mazda MX-5 na servisu"),
    ("Servis_mazda_2_01.jpg", "mazda2", "Mazda 2"),
    ("Servis_mazda_2_02_.jpg", "mazda2", "Mazda 2"),
    ("Servis_mazda_2_03.jpg", "mazda2", "Mazda 2"),
    ("Servis_mazda_2_04.jpg", "mazda2", "Mazda 2"),
    ("Servis_mazda_2_05.jpg", "mazda2", "Mazda 2"),
    ("Servis_mazda_3_01.jpg", "mazda3", "Mazda 3"),
    ("Servis_mazda_3_02.jpg", "mazda3", "Mazda 3"),
    ("Servis_mazda_6.jpg", "mazda6", "Mazda 6"),
] + [(f"Servis_mazda_6_{i:02d}.jpg", "mazda6", "Mazda 6") for i in range(1, 11)] + [
    ("Servis_cx5_i_cx7.jpg", "cx", "Mazda CX-5 i CX-7"),
    ("Servis_cx7.jpg", "cx", "Mazda CX-7"),
]
FILTERS = [("sve", "Sve"), ("radionica", "Radionica i dijagnostika"), ("mazda2", "Mazda 2"),
           ("mazda3", "Mazda 3"), ("mazda6", "Mazda 6"), ("cx", "CX modeli"), ("mx5", "MX-5")]

# (brend, sajt, logo u img/delovi/)
PARTS = [
    ("Motorna ulja", [("Total", "https://lubricants.totalenergies.com/", "header-logo-total.png"),
                      ("Mobil", "https://www.mobil.com/", "mobil.png")]),
    ("Kočioni sistemi i amortizeri", [("ATE", "https://www.ate-brakes.com/", "logo_ate.png"),
                                      ("Brembo", "https://www.brembo.com/", "logo_brembo.gif"),
                                      ("Galfer", "https://www.galfer-aftermarket.com/", "logo_auto.png"),
                                      ("KYB", "https://www.kyb-europe.com/", "KYB_logo.jpg")]),
    ("Setovi kvačila", [("LuK", "https://www.schaeffler.com/", "LuK_logo.png"),
                        ("Sachs", "https://www.zf.com/", "Sachs.jpg")]),
    ("Zupčenje", [("Gates PowerGrip", "https://www.gates.com/", "PowerGrip.jpg"),
                  ("SKF", "https://www.skf.com/", "Skf_logo.png"),
                  ("Blue Print", "https://www.blue-print.com/", "logo-blue-print.jpg"),
                  ("Dayco", "https://www.dayco.com/", "dayco.png")]),
    ("Elektronika i paljenje", [("Denso", "https://www.denso.com/", "denso.png"),
                                ("NGK", "https://www.ngk.com/", "NGK.jpg")]),
    ("Ležajevi", [("SKF", "https://www.skf.com/", "Skf_logo.png"),
                  ("NTN", "https://www.ntnglobal.com/", "NTN_logo.png"),
                  ("INA", "https://www.schaeffler.com/", "ina-auto-parts.jpg"),
                  ("BTA", "https://bta-bearings.com/", "Bta_logo.JPG")]),
    ("Trap i vešanje", [("Sidem", "https://www.sidem.be/", "Sidem_logo.jpg"),
                        ("Delphi", "https://www.delphiautoparts.com/", "delphi-auto-parts.jpg"),
                        ("Lemförder (ZF)", "https://www.zf.com/", "lemforder_banner.jpg")]),
]


def write(name, html):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), "w", encoding="utf-8") as f:
        f.write(html)


# Servisni tim: (fotografija ili None, ime, uloga). Fotografija npr. "img/tim/marko.jpg", format 4:5.
TEAM = [
    (None, "Ime Prezime", "Vlasnik i šef servisa"),
    (None, "Ime Prezime", "Automehaničar"),
    (None, "Ime Prezime", "Automehaničar"),
    (None, "Ime Prezime", "Dijagnostika i elektrika"),
]
PLACEHOLDER = '<div class="team-ph" role="img" aria-label="Mesto za fotografiju"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg><span>Fotografija</span></div>'
def team_photo(ph, name):
    return PLACEHOLDER if not ph else '<img src="%s" alt="%s" loading="lazy">' % (ph, name)


team_html = "\n".join(
    '      <li>%s<h3 class="h3">%s</h3><p>%s</p></li>' % (team_photo(ph, n), n, r)
    for ph, n, r in TEAM)

# ---------------- MODELI: linkovanje ----------------
# Naziv modela -> fajl pojedinačne strane. Kada model dobije stranu, dodati ga
# ovde i wall() ga automatski pretvara u link. Modeli bez unosa ostaju običan tekst.
MODEL_PAGES = {
    "Mazda 2": "mazda-2.html",
}


def model_link(name):
    href = MODEL_PAGES.get(name)
    return f'<a href="{href}">{name}</a>' if href else name


def wall(models):
    return '<ul class="model-wall">' + "".join(f"<li>{model_link(m)}</li>" for m in models) + "</ul>"


# ---------------- NASLOVNA ----------------
jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"AutoRepair","name":"EAST Auto Servis","url":"https://eastservis.rs",
"telephone":"{PHONE}","email":"{EMAIL}","foundingDate":"2010",
"description":"Specijalizovani servis za Mazda vozila u Beogradu.",
"address":{{"@type":"PostalAddress","streetAddress":"Slanački put 123a","addressLocality":"Beograd","addressRegion":"Višnjička Banja","addressCountry":"RS"}},
"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}}],
"geo":{{"@type":"GeoCoordinates","latitude":44.81298,"longitude":20.54062}},
"sameAs":["{FB}"]}}
</script>
"""

teaser_imgs = ["Servis_mazde.jpg", "Servis_mx5.jpg", "Servis_mazda_6_03.jpg",
               "Servis_mazda_dijagnostika_02.jpg", "Servis_cx5_i_cx7.jpg"]
teaser = "\n".join(
    f'      <a href="galerija.html"><img src="{IMG}galerija/{"" if i == 0 else "mala/"}{f}" alt="Fotografija iz servisa" loading="lazy"></a>'
    for i, f in enumerate(teaser_imgs))

index = head("EAST Auto Servis | Mazda servis Beograd",
             "Specijalizovani Mazda servis na Slanačkom putu u Beogradu od 2010. Redovan servis, kompjuterska dijagnostika, remont motora i pregled vozila pre kupovine.",
             "index.html", jsonld + '<script src="js/hero-rev.js" defer></script>\n') + f"""<section class="hero" style="background-image:url('{IMG}galerija/Servis_mazde.jpg')">
  <video class="hero-media" autoplay muted loop playsinline preload="metadata" poster="{IMG}galerija/Servis_mazde.jpg" aria-hidden="true">
    <source src="video/hero.webm" type="video/webm">
    <source src="video/hero.mp4" type="video/mp4">
  </video>
  <button class="hero-sound" type="button" aria-pressed="false" aria-label="Uključi zvuk motora">{ICON_SOUND}<span class="hero-sound-txt">Zvuk</span></button>
  <div class="wrap hero-content">
    <h1>Servis za vašu Mazdu.</h1>
    <p class="lead">Specijalizovani Mazda servis u Beogradu od 2010. Redovno održavanje, dijagnostika Mazda opremom i remont motora, uz pisani izveštaj o stanju vozila posle svake intervencije.</p>
    <div class="hero-actions">
      <a class="btn btn-red" href="kontakt.html">{ICON_CAL}Zakažite servis</a>
      <a class="btn btn-ghost" href="tel:{PHONE}">{ICON_PHONE}{PHONE_TXT}</a>
    </div>
    <div class="tach" aria-hidden="true">
      <div class="tach-scale"><div class="tach-fill"></div></div>
      <div class="tach-labels"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span></div>
      <div class="tach-unit">×1000 o/min</div>
    </div>
    <ul class="facts">
      <li><strong>Od 2010.</strong><span>radimo samo Mazde</span></li>
      <li><strong>500+ klijenata</strong><span>vraća se redovno</span></li>
      <li><strong>15 sertifikata</strong><span>Mazda obuka mehaničara</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <h2 class="h2">Jedna marka, šesnaest godina iskustva.</h2>
    <div class="measure">
      <p class="lead">Mazdu znamo do poslednjeg šrafa. Od Mazde 2 do najnovijih CX modela, radimo na njima svakog dana.</p>
      <p class="muted">Naši mehaničari imaju međunarodne Mazda sertifikate, a radionica je od 2012. proširena na više potpuno opremljenih radnih mesta. Održavamo pojedinačna vozila i vozne parkove.</p>
      <p><a class="link" href="o-nama.html">Više o servisu</a></p>
    </div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Šta radimo</h2>
      <p>Posle svake intervencije dobijate izveštaj: šta je urađeno, šta smo primetili i šta preporučujemo za sledeći servis.</p>
    </div>
    <ul class="service-list">
      <li><h3 class="h3">Redovan servis</h3><p>Mali i veliki servis po Mazda intervalima: ulje, filteri, svećice, tečnosti i provera svih sklopova.</p><a class="link" href="servis.html#redovan">Detalji</a></li>
      <li><h3 class="h3">Kompjuterska dijagnostika</h3><p>Specijalizovana dijagnostika za Mazda vozila. Dobijate izveštaj sa očitanim parametrima i greškama.</p><a class="link" href="servis.html#dijagnostika">Detalji</a></li>
      <li><h3 class="h3">Pregled pre kupovine</h3><p>Kupujete polovnu Mazdu? Proveravamo motor, pogon, trap, kočnice i elektriku pre nego što platite.</p><a class="link" href="servis.html#pregled">Detalji</a></li>
      <li><h3 class="h3">Generalni remont motora</h3><p>Kompletan remont sa proverom svih pomoćnih agregata. Na urađen remont dajemo garanciju.</p><a class="link" href="servis.html#remont">Detalji</a></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Kako izgleda servis kod nas</h2>
      <p>Bez iznenađenja na računu. Svaki dodatni rad dogovaramo sa vama pre nego što počnemo.</p>
    </div>
    <ol class="steps">
      <li><h3>Zakazivanje</h3><p>Pozovite ili pošaljite upit. Dogovaramo termin koji vam odgovara.</p></li>
      <li><h3>Prijem vozila</h3><p>Zapisujemo kilometražu, simptome i šta želite da uradimo.</p></li>
      <li><h3>Dijagnostika</h3><p>Proveravamo vozilo i javljamo vam nalaz i procenu troška.</p></li>
      <li><h3>Rad</h3><p>Radimo samo ono što ste odobrili, sa proverenim delovima.</p></li>
      <li><h3>Predaja i izveštaj</h3><p>Preuzimate auto uz izveštaj i preporuke za sledeći servis.</p></li>
    </ol>
  </div>
</section>

<section class="section section-ink">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Modeli koje servisiramo</h2>
      <p>Od najnovijih SUV-ova do rotacionih RX modela. Starije Mazde radimo uz prethodni dogovor.</p>
    </div>
    {wall(["Mazda 2", "Mazda 3", "Mazda 5", "Mazda 6", "CX-3", "CX-30", "CX-5", "CX-60", "CX-7", "MX-30", "MX-5", "RX-7", "RX-8"])}
    <p class="mt"><a class="link" href="modeli.html">Kompletan spisak modela</a></p>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Naš servisni tim</h2>
      <p>Sertifikovani Mazda mehaničari koji će raditi na vašem vozilu.</p>
    </div>
    <ul class="team">
{team_html}
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Iz radionice</h2>
      <p><a class="link" href="galerija.html">Pogledajte celu galeriju</a></p>
    </div>
    <div class="teaser">
{teaser}
    </div>
  </div>
</section>

<section class="section section-ink" id="kontakt">
  <div class="wrap contact-band">
    <div>
      <h2 class="h2">Zakažite termin</h2>
      <a class="big-phone" href="tel:{PHONE}">{PHONE_TXT}</a>
      <dl class="contact-lines">
        <div><dt>Mejl</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>Radno vreme</dt><dd>Ponedeljak–petak 08–17 h, vikendom ne radimo</dd></div>
        <div><dt>Adresa</dt><dd><a href="{MAP_LINK}" target="_blank" rel="noopener">{ADDRESS}</a></dd></div>
      </dl>
      <a class="btn btn-red" href="kontakt.html">{ICON_CAL}Pošaljite upit za termin</a>
    </div>
    <div class="map"><iframe src="{MAP}" title="Lokacija servisa na mapi" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
""" + foot()
write("index.html", index)

# ---------------- SERVIS I DELOVI ----------------
parts_html = "\n".join(
    f'      <div><dt>{cat}</dt><dd>' + "".join(
        f'<a class="brand-logo" href="{u}" target="_blank" rel="noopener" aria-label="{b}">'
        f'<img src="img/delovi/{lg}" alt="{b}" loading="lazy"></a>' for b, u, lg in brands) + "</dd></div>"
    for cat, brands in PARTS)

servis = head("Servis i delovi | EAST Auto Servis",
              "Redovan servis, kompjuterska dijagnostika, pregled polovnog vozila i generalni remont Mazda motora. Ugrađujemo delove proverenih proizvođača.",
              "servis.html") + page_head("Servis i delovi",
              "Kompletno održavanje Mazda vozila na jednom mestu. Posle svake intervencije dobijate pisani izveštaj o stanju vozila.") + f"""
<section class="section">
  <div class="wrap">
    <article class="service-detail" id="redovan">
      <h2 class="h2">Redovan servis</h2>
      <div class="measure">
        <p>Mali i veliki servis radimo po intervalima koje propisuje Mazda za vaš model i motor. Sve nedostatke koje primetimo i predloge za buduće intervencije upisujemo u izveštaj koji dobijate uz vozilo.</p>
        <ul><li>Zamena ulja i svih filtera</li><li>Svećice, tečnosti i kaiševi</li><li>Provera kočnica, trapa i pneumatika</li><li>Resetovanje servisnog intervala</li></ul>
      </div>
    </article>
    <article class="service-detail" id="dijagnostika">
      <h2 class="h2">Kompjuterska dijagnostika</h2>
      <div class="measure">
        <p>Koristimo dijagnostičku opremu specijalizovanu za Mazda vozila. Dobijate izveštaj sa očitanim parametrima i greškama, uz objašnjenje šta koja greška znači i šta je potrebno uraditi.</p>
        <ul><li>Očitavanje i brisanje grešaka</li><li>Praćenje parametara motora u radu</li><li>Provera elektronike i senzora</li></ul>
      </div>
    </article>
    <article class="service-detail" id="pregled">
      <h2 class="h2">Pregled pre kupovine</h2>
      <div class="measure">
        <p>Ako kupujete polovnu Mazdu ili želite da znate u kakvom je stanju vaš auto, dovezite ga na servisni pregled. Pregledamo sve grupe na vozilu i rezultate vam predstavimo pre nego što donesete odluku.</p>
        <ul><li>Motorna grupa i pogon</li><li>Trap i kočioni sistem</li><li>Elektrika i instalacija</li><li>Kompjuterska dijagnostika</li></ul>
      </div>
    </article>
    <article class="service-detail" id="remont">
      <h2 class="h2">Generalni remont motora</h2>
      <div class="measure">
        <p>Uz generalni remont proveravamo i sve pomoćne agregate, kako bi motor posle remonta radio pouzdano. Na izvršen remont dajemo garanciju.</p>
        <ul><li>Rastavljanje, merenje i procena</li><li>Zamena potrošnih i oštećenih delova</li><li>Provera turbine, dizni i pomoćnih agregata</li></ul>
      </div>
    </article>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Česti radovi</h2>
      <p>Ako vaš kvar nije na spisku, pozovite nas. Verovatno smo ga već rešavali.</p>
    </div>
    <ul class="jobs">
      <li>Zamena ulja</li><li>Mali servis</li><li>Veliki servis</li><li>Zupčasti kaiš i lanac</li><li>Kočnice</li><li>Kvačilo</li><li>Plivajući zamajac</li><li>Dizne</li><li>Turbina</li><li>Trap i vešanje</li><li>Amortizeri</li><li>Ležajevi</li><li>Elektrika</li><li>Klima uređaj</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Delovi koje ugrađujemo</h2>
      <p>Preporučujemo samo delove renomiranih svetskih proizvođača. Ako želite originalne Mazda delove, nabavićemo ih.</p>
    </div>
    <dl class="parts">
{parts_html}
    </dl>
  </div>
</section>
""" + CTA + foot()
write("servis.html", servis)

# ---------------- MODELI ----------------
modeli = head("Modeli koje servisiramo | EAST Auto Servis",
              "Servisiramo Mazda vozila: Mazda 2, 3, 5, 6, CX-3, CX-30, CX-5, CX-60, CX-7, MX-30, MX-5, Wankel motore RX-7 i RX-8, a uz prethodni dogovor i starije modele 323, 626, 929 i Xedos.",
              "modeli.html") + page_head("Modeli koje servisiramo",
              "Od današnjih hibrida i SUV-ova do Wankel motora. Starije Mazde radimo uz prethodni dogovor.") + f"""
<section class="section">
  <div class="wrap">
    <div class="model-group">
      <div><h2 class="h2">Aktuelni modeli</h2><p>Novija vozila, uključujući Skyactiv benzince, dizele i hibride.</p></div>
      {wall(["Mazda 2", "Mazda 3", "Mazda 6", "CX-3", "CX-30", "CX-5", "CX-60", "MX-30", "MX-5"])}
    </div>
    <div class="model-group">
      <div><h2 class="h2">Prethodne generacije</h2><p>Modeli koji se više ne prodaju, a i dalje su česti na ulicama.</p></div>
      {wall(["Mazda 5", "CX-7", "Mazda 3 MPS", "Mazda 6 MPS"])}
    </div>
    <div class="model-group">
      <div><h2 class="h2">Wankel motori</h2><p>Rotacioni motori traže posebno znanje, od kompresije i dihtovanja rotora do podmazivanja. Mi ga imamo.</p></div>
      {wall(["RX-7", "RX-8"])}
    </div>
    <div class="model-group">
      <div><h2 class="h2">Stariji modeli</h2><p>Vozila starija od 2010. radimo uz prethodni dogovor. Pozovite pre dolaska, pa ćemo rado pogledati i vašeg „dedu“.</p><p><a class="link" href="tel:{PHONE}">Pozovite {PHONE_TXT}</a></p></div>
      {wall(["121", "323", "323F", "626", "929", "Xedos 6", "Xedos 9", "MX-3", "MX-6", "Premacy", "MPV", "Demio"])}
    </div>
  </div>
</section>

""" + CTA + foot()
write("modeli.html", modeli)

# ---------------- POJEDINAČNE STRANE MODELA ----------------
# "gens": (naziv generacije, godine, karoserija, motori) — činjenice.
# "service": (naslov, opis) — NACRT servisnih tačaka, klijent potvrđuje za svaki model.
MODELS = {
    "mazda-2.html": {
        "name": "Mazda 2",
        "title": "Servis za Mazdu 2 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za sve generacije Mazde 2 (DY, DE, DJ) u Beogradu. Redovan servis, lanac razvoda, Skyactiv motori i pregled pre kupovine.",
        "lead": "Servisiramo sve generacije Mazde 2, od prvih MZI benzinaca do današnjih Skyactiv motora.",
        "photo": "mazda2-dimenzije.webp",
        "diagram": True,
        "blueprint": "mazda2-blueprint-2019.webp",
        "intro": ('<p class="lead">Mazda 2 je gradski automobil koji vozači biraju zbog jednostavnosti i niskih troškova održavanja. '
                  'Baš zato je važno da servis rade ljudi koji model dobro poznaju.</p>'
                  '<p class="muted">Kroz našu radionicu prošlo je više generacija Mazde 2, od benzinaca sa lancem razvoda do Skyactiv motora. '
                  'Radimo redovan servis, dijagnostiku i popravke, uz pisani izveštaj o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (DY)", "2002–2007", "Hečbek s pet vrata.",
             "Benzin: 1.25, 1.3, 1.4, 1.5 i 1.6. Dizel: 1.4 MZ-CDTi."),
            ("2. generacija (DE)", "2007–2014", "Hečbek s tri i pet vrata i limuzina.",
             "Benzin: 1.3 i 1.5, kasnije 1.3 Skyactiv-G. Dizel: 1.4 i 1.6."),
            ("3. generacija (DJ)", "2014–danas", "Hečbek s pet vrata i limuzina.",
             "Benzin: 1.3, 1.5 i 2.0 Skyactiv-G i 1.5 Skyactiv-Hybrid. Dizel: 1.5 Skyactiv-D (do 2019)."),
        ],
        "service": [
            ("Lanac razvoda i paljenje",
             "Kod benzinaca proveravamo zategnutost lanca razvoda i stanje bobina i svećica, jer neravnomeran rad motora najčešće počinje odatle."),
            ("Skyactiv-G i ubrizgavanje",
             "Na Skyactiv benzincima pratimo rad ubrizgavanja i po potrebi čistimo usisni trakt i lambda sonde."),
            ("Kočnice i zadnja osovina",
             "Gradska vožnja najviše troši kočnice; proveravamo diskove, pločice i ležajeve zadnje grede."),
            ("Klima i elektrika",
             "Proveravamo punjenje klime, alternator i akumulator, česte tačke kod manjih gradskih automobila."),
        ],
    },
}


def gen_cards(gens):
    return "\n".join(
        f'      <li><h3 class="h3">{title} · {years}</h3><p>{body} {engines}</p></li>'
        for title, years, body, engines in gens)


def service_cards(items):
    return "\n".join(
        f'      <li><h3 class="h3">{h}</h3><p>{p}</p></li>' for h, p in items)


def model_page(slug, m):
    diagram = m.get("diagram")
    img_cls = "model-photo is-diagram" if diagram else "model-photo"
    img_dir = "img/modeli/" if diagram else "img/galerija/"
    img_alt = f"Dimenzije modela {m['name']}" if diagram else f"{m['name']} u servisu EAST Auto Servis"
    blueprint = (f'\n      <img class="model-blueprint" src="img/modeli/{m["blueprint"]}" '
                 f'alt="Tehnički crtež modela {m["name"]} sa merama" loading="lazy">' if m.get("blueprint") else "")
    html = head(m["title"], m["desc"], "modeli.html") + page_head(m["name"], m["lead"]) + f"""
<section class="section">
  <div class="wrap split">
    <div class="model-intro">
      <h2>Servis za {m['name']}</h2>
      <img class="{img_cls}" src="{img_dir}{m['photo']}" alt="{img_alt}" loading="lazy">
    </div>
    <div class="measure">
      {m['intro']}{blueprint}
    </div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Generacije koje servisiramo</h2>
      <p>Radimo sve generacije modela {m['name']} zastupljene na našem tržištu.</p>
    </div>
    <ul class="service-list">
{gen_cards(m['gens'])}
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Na šta obraćamo pažnju</h2>
      <p>Tipične tačke održavanja i česti radovi kod ovog modela.</p>
    </div>
    <ul class="service-list">
{service_cards(m['service'])}
    </ul>
  </div>
</section>
""" + CTA + foot()
    write(slug, html)


for _slug, _m in MODELS.items():
    model_page(_slug, _m)

# ---------------- SERTIFIKATI ----------------
certs = "\n".join(
    f'      <a href="{IMG}sertifikati/Sertifikat_{i:02d}.JPG" data-lb="cert" data-caption="Mazda sertifikat {i} od 15">'
    f'<img src="{IMG}sertifikati/mala/Sertifikat_{i:02d}.JPG" alt="Mazda sertifikat mehaničara, {i} od 15" loading="lazy"></a>'
    for i in range(1, 16))
sert = head("Sertifikati | EAST Auto Servis",
            "Mehaničari EAST Auto Servisa imaju 15 međunarodnih Mazda sertifikata za servis i dijagnostiku.",
            "sertifikati.html") + page_head("Sertifikati",
            "Iskustvo iz radionice potvrđeno je sa 15 Mazda sertifikata. Kliknite na sertifikat da ga pogledate u punoj veličini.") + f"""
<section class="section">
  <div class="wrap">
    <div class="thumb-grid certs">
{certs}
    </div>
  </div>
</section>
""" + CTA + foot(lightbox=True)
write("sertifikati.html", sert)

# ---------------- GALERIJA ----------------
filters = "".join(
    f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "sve" else "false"}">{n}</button>'
    for k, n in FILTERS)
gal = "\n".join(
    f'      <a href="{IMG}galerija/{f}" data-lb="gal" data-cat="{c}" data-caption="{cap}">'
    f'<img src="{IMG}galerija/mala/{f}" alt="{cap}" loading="lazy"></a>'
    for f, c, cap in GALLERY)
galerija = head("Galerija | EAST Auto Servis",
                "Fotografije iz EAST Mazda servisa: radionica, dijagnostika i vozila na servisu.",
                "galerija.html") + page_head("Galerija",
                "Radionica, dijagnostika i Mazde koje su prošle kroz naše ruke.") + f"""
<section class="section">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtriraj fotografije">{filters}</div>
    <p class="count" aria-live="polite"></p>
    <div class="thumb-grid">
{gal}
    </div>
  </div>
</section>
""" + CTA + foot(lightbox=True)
write("galerija.html", galerija)

# ---------------- O NAMA ----------------
onama = head("O nama | EAST Auto Servis",
             "EAST Auto Servis je otvoren 2010. godine kao specijalizovani Mazda servis u Beogradu. Sertifikovani mehaničari i više od 500 stalnih klijenata.",
             "o-nama.html") + page_head("O nama",
             "Otvorili smo servis 2010. sa jednom idejom: da radimo samo Mazde i da ih radimo kako treba.") + f"""
<section class="section">
  <div class="wrap split">
    <div>
      <h2 class="h2">Ko smo mi</h2>
    </div>
    <div class="measure">
      <p class="lead">EAST Auto Servis je specijalizovan za vozila marke Mazda. Naši mehaničari imaju višegodišnje iskustvo i međunarodne Mazda sertifikate.</p>
      <p class="muted">Stalno ulaganje u opremu i obuku omogućilo nam je da danas imamo više od 500 klijenata koji nam se vraćaju. Kod nas možete kompletno održavati svoje vozilo ili ceo vozni park: od automehanike i dijagnostike do popravki.</p>
      <img class="photo-wide mt" src="{IMG}galerija/Servis_mazda_dijagnostika_01.jpg" alt="Mazda na dijagnostici u radionici" loading="lazy">
    </div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head"><h2 class="h2">Kako smo rasli</h2></div>
    <ol class="timeline">
      <li><span class="year">2010</span><div><h3 class="h3">Otvaranje servisa</h3><p>Počinjemo kao servis specijalizovan isključivo za Mazda vozila.</p></div></li>
      <li><span class="year">2012</span><div><h3 class="h3">Proširenje radionice</h3><p>Servis dobija više radnih mesta, svako kompletno opremljeno potrebnim alatom.</p></div></li>
      <li><span class="year">Danas</span><div><h3 class="h3">Više od 500 stalnih klijenata</h3><p>Petnaest Mazda sertifikata, savremena dijagnostika i klijenti koji nam poveravaju i svoje vozne parkove.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section-ink">
  <div class="wrap">
    <div class="section-head"><h2 class="h2">Na čemu insistiramo</h2></div>
    <ul class="values">
      <li><h3 class="h3">Znate šta plaćate</h3><p>Svaki rad dogovaramo pre početka. Na kraju dobijate izveštaj o stanju vozila i preporuke.</p></li>
      <li><h3 class="h3">Provereni delovi</h3><p>Ugrađujemo delove renomiranih proizvođača ili originalne Mazda delove, po vašem izboru.</p></li>
      <li><h3 class="h3">Garancija na rad</h3><p>Na generalni remont motora dajemo garanciju. Iza svog posla stojimo.</p></li>
    </ul>
  </div>
</section>
""" + CTA + foot()
write("o-nama.html", onama)

# ---------------- KONTAKT ----------------
kontakt = head("Kontakt i zakazivanje | EAST Auto Servis",
               "Zakažite servis za vašu Mazdu. Slanački put 123a, Višnjička Banja, Beograd. Telefon 064 144 63 43, radimo radnim danima 08–17 h.",
               "kontakt.html") + page_head("Kontakt i zakazivanje",
               "Najbrže je da nas pozovete. Ako vam je lakše, pošaljite upit i javićemo vam se sa slobodnim terminom.") + f"""
<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <form class="form" id="booking" novalidate>
        <div class="field"><label for="ime">Ime i prezime</label><input id="ime" name="ime" autocomplete="name" required></div>
        <div class="field"><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" autocomplete="tel" inputmode="tel" required></div>
        <div class="field"><label for="model">Model i godište <span class="hint">(npr. Mazda 6, 2015)</span></label><input id="model" name="model"></div>
        <div class="field"><label for="usluga">Usluga</label>
          <select id="usluga" name="usluga">
            <option>Redovan servis</option>
            <option>Kompjuterska dijagnostika</option>
            <option>Pregled pre kupovine</option>
            <option>Generalni remont motora</option>
            <option>Kvar ili nešto drugo</option>
          </select></div>
        <div class="field full"><label for="termin">Željeni termin <span class="hint">(opciono)</span></label><input id="termin" name="termin" placeholder="npr. utorak pre podne"></div>
        <div class="field full"><label for="poruka">Opišite problem <span class="hint">(opciono)</span></label><textarea id="poruka" name="poruka"></textarea></div>
        <div class="full"><button class="btn btn-red" type="submit">{ICON_CAL}Pošaljite upit</button></div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>

      <aside>
        <div class="info-block"><h2>Telefon</h2><a class="phone" href="tel:{PHONE}">{PHONE_TXT}</a></div>
        <div class="info-block"><h2>Mejl</h2><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="info-block"><h2>Radno vreme</h2>
          <dl class="hours"><dt>Ponedeljak–petak</dt><dd>08–17 h</dd><dt>Subota i nedelja</dt><dd>Ne radimo</dd></dl></div>
        <div class="info-block"><h2>Adresa</h2><a href="{MAP_LINK}" target="_blank" rel="noopener">Slanački put 123a<br>Višnjička Banja, Beograd</a></div>
        <div class="info-block"><h2>Društvene mreže</h2><a href="{FB}" target="_blank" rel="noopener">Facebook: East Auto Servis</a></div>
      </aside>
    </div>
    <div class="map-full"><iframe src="{MAP}" title="Lokacija servisa na mapi" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
""" + foot()
write("kontakt.html", kontakt)

print("Generisano:", ", ".join(p for p, _ in PAGES))
