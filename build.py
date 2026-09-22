#!/usr/bin/env python3
"""Generiše statičke HTML strane za eastservis.rs (zajednički header/footer).
Slike se trenutno učitavaju sa postojećeg sajta (IMG). Kada se folder img/
prekopira u projekat, promeniti IMG u "img/" i ponovo pokrenuti: python3 build.py
"""
import os
import re

IMG = "https://eastservis.rs/img/"
# Apsolutna baza za og:image / deljenje na mrežama. PROMENITI na https://eastservis.rs u produkciji.
BASE_URL = "https://mrpaki.github.io/mazda"
PHONE = "+381641446343"
PHONE_TXT = "064 144 63 43"
EMAIL = "office@eastservis.rs"
FB = "https://www.facebook.com/eastautoservis"
IG = "https://www.instagram.com/east_mazda_servis/"
MAP = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2830.421125364123!2d20.540623215535767"
       "!3d44.81298467909866!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x475a7a3ecfc94c91%3A"
       "0x3dd3f6d00bd5e0ab!2sMazda+Servis%22East+Auto+Servis%22!5e0!3m2!1ssr!2srs!4v1486586850562")
ADDRESS = "Slanački put 123a, Višnjička Banja, Beograd"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Slana%C4%8Dki+put+123a+Beograd"

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'
ICON_SOUND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4z"/><path class="snd-off" d="M22 9l-6 6M16 9l6 6"/><path class="snd-on" d="M15.5 8.5a5 5 0 0 1 0 7M19 5a9 9 0 0 1 0 14"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>'
SOCIAL = f'<span class="social"><a href="{FB}" target="_blank" rel="noopener" aria-label="EAST Auto Servis na Facebook-u">{ICON_FB}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="EAST Auto Servis na Instagram-u">{ICON_IG}</a></span>'

PAGES = [
    ("index.html", "Naslovna"),
    ("servis.html", "Servis i delovi"),
    ("modeli.html", "Modeli"),
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
      <span class="brand-name">EAST<span class="brand-jp" lang="ja">ひがし</span></span>
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
        <a class="brand" href="index.html"><span class="brand-name">EAST<span class="brand-jp" lang="ja">ひがし</span></span><span class="brand-sub">Mazda servis Beograd</span></a>
        <p>Specijalizovani servis za Mazda vozila od 2000. godine. Redovno održavanje, dijagnostika i remont.</p>
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
          <li>{SOCIAL}</li>
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
    "Mazda 3": "mazda-3.html",
    "Mazda 6": "mazda-6.html",
    "CX-3": "cx-3.html",
    "CX-30": "cx-30.html",
    "CX-5": "cx-5.html",
}


def model_link(name):
    href = MODEL_PAGES.get(name)
    return f'<a href="{href}">{name}</a>' if href else name


def wall(models):
    return '<ul class="model-wall">' + "".join(f"<li>{model_link(m)}</li>" for m in models) + "</ul>"


# ---------------- NASLOVNA ----------------
jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"AutoRepair","name":"EAST Auto Servis","url":"https://eastservis.rs",
"telephone":"{PHONE}","email":"{EMAIL}","foundingDate":"2000",
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
             "Specijalizovani Mazda servis na Slanačkom putu u Beogradu od 2000. Redovan servis, kompjuterska dijagnostika, remont motora i pregled vozila pre kupovine.",
             "index.html", jsonld + '<script src="js/hero-rev.js" defer></script>\n') + f"""<section class="hero" style="background-image:url('{IMG}galerija/Servis_mazde.jpg')">
  <video class="hero-media" autoplay muted loop playsinline preload="metadata" poster="{IMG}galerija/Servis_mazde.jpg" aria-hidden="true">
    <source src="video/hero.webm" type="video/webm">
    <source src="video/hero.mp4" type="video/mp4">
  </video>
  <button class="hero-sound" type="button" aria-pressed="false" aria-label="Uključi zvuk motora">{ICON_SOUND}<span class="hero-sound-txt">Zvuk</span></button>
  <div class="wrap hero-content">
    <h1>Servis za vašu Mazdu.</h1>
    <p class="lead">Specijalizovani Mazda servis u Beogradu od 2000. Redovno održavanje, dijagnostika Mazda opremom i remont motora, uz pisani izveštaj o stanju vozila posle svake intervencije.</p>
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
      <li><strong>Od 2000.</strong><span>radimo samo Mazde</span></li>
      <li><strong>1500+ klijenata</strong><span>vraća se redovno</span></li>
      <li><strong>15 sertifikata</strong><span>Mazda obuka mehaničara</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <h2 class="h2">Jedna marka, dvadeset šest godina iskustva.</h2>
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
        "photo": "mazda2-blueprint-2019.webp",
        "diagram": True,
        "photo_alt": "Dimenzije i proporcije modela Mazda 2 (tehnički crtež)",
        "intro": ('<p class="lead">Mazda 2 je gradski automobil koji vozači biraju zbog jednostavnosti i niskih troškova održavanja. '
                  'Baš zato je važno da servis rade ljudi koji model dobro poznaju.</p>'
                  '<p class="muted">Kroz našu radionicu prošlo je više generacija Mazde 2, od benzinaca sa lancem razvoda do Skyactiv motora. '
                  'Radimo redovan servis, dijagnostiku i popravke, uz pisani izveštaj o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (DY)", "2003–2007", "Hečbek s tri i pet vrata.",
             "mazda2-dy.webp", [
                ("1.25", "Benzin", "1.242 cm³", "75 KS"),
                ("1.4", "Benzin", "1.388 cm³", "80 KS"),
                ("1.6", "Benzin", "1.596 cm³", "100 KS"),
                ("1.4 MZ-CDTi", "Dizel", "1.399 cm³", "68 KS"),
             ]),
            ("2. generacija (DE/DH)", "2007–2014", "Hečbek s tri i pet vrata i limuzina.",
             "mazda2-de.webp", [
                ("1.3", "Benzin", "1.349 cm³", "75–86 KS"),
                ("1.5", "Benzin", "1.498 cm³", "103 KS"),
                ("1.4 MZ-CD", "Dizel", "1.399 cm³", "68 KS"),
                ("1.6 MZ-CD", "Dizel", "1.560 cm³", "90 KS"),
             ]),
            ("3. generacija (DJ)", "2014–danas", "Hečbek s pet vrata i limuzina. Kroz proizvodnju je dva puta redizajnirana (2019. i 2023). "
             "Od 2022. paralelno se prodaje i Mazda2 Hybrid (XP210), tehnički baziran na Toyoti Yaris.",
             "mazda2-dj.webp", [
                ("1.3 Skyactiv-G", "Benzin", "1.298 cm³", "90–93 KS"),
                ("1.5 Skyactiv-G", "Benzin", "1.496 cm³", "75–115 KS"),
                ("1.5 e-Skyactiv G (M Hybrid)", "Benzin (MHEV)", "1.496 cm³", "90–115 KS"),
                ("1.5 Skyactiv-D", "Dizel", "1.499 cm³", "105 KS"),
             ], [
                ("Redizajn 2019", "mazda2-dj-2019.webp"),
                ("Redizajn 2023", "mazda2-dj-2023.webp"),
             ]),
        ],
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora.",
        "photo_credit": ('Fotografije generacija: Wikimedia Commons — '
                         'M 93 (CC BY-SA 3.0 DE), OSX (javno vlasništvo), EurovisionNim i '
                         'Alexander Migl (CC BY-SA 4.0).'),
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
    "mazda-3.html": {
        "name": "Mazda 3",
        "title": "Servis za Mazdu 3 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za sve generacije Mazde 3 (BK, BL, BM, BP) u Beogradu. MZR benzinci, Skyactiv-G i Skyactiv-D motori, lanac razvoda, DPF i pregled pre kupovine.",
        "lead": "Servisiramo sve generacije Mazde 3, od prvih MZR benzinaca do današnjih Skyactiv i Skyactiv-X motora.",
        "photo": "mazda3-dimenzije.webp",
        "diagram": True,
        "photo_alt": "Dimenzije i proporcije modela Mazda 3 (tehnički crtež)",
        "intro": ('<p class="lead">Mazda 3 je jedan od najprodavanijih Mazda modela kod nas, u obe karoserije, hečbek i limuzinu. '
                  'Kroz našu radionicu prošle su sve četiri generacije, pa svaku od njih dobro poznajemo.</p>'
                  '<p class="muted">Radimo od starijih MZR benzinaca i dizela do Skyactiv-G, Skyactiv-D i Skyactiv-X motora. '
                  'Redovan servis, dijagnostiku Mazda opremom i popravke pratimo pisanim izveštajem o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (BK)", "2003–2009", "Hečbek s pet vrata i limuzina.",
             "mazda3-bk.webp", [
                ("1.4 MZR", "Benzin", "1.349 cm³", "84 KS"),
                ("1.6 MZR", "Benzin", "1.598 cm³", "105 KS"),
                ("2.0 MZR", "Benzin", "1.999 cm³", "150 KS"),
                ("2.3 DISI Turbo (MPS)", "Benzin", "2.261 cm³", "260 KS"),
                ("1.6 MZR-CD", "Dizel", "1.560 cm³", "90–109 KS"),
                ("2.0 MZR-CD", "Dizel", "1.998 cm³", "143 KS"),
             ]),
            ("2. generacija (BL)", "2009–2013", "Hečbek s pet vrata i limuzina.",
             "mazda3-bl.webp", [
                ("1.6 MZR", "Benzin", "1.598 cm³", "105 KS"),
                ("2.0 MZR", "Benzin", "1.999 cm³", "150 KS"),
                ("2.3 DISI Turbo (MPS)", "Benzin", "2.261 cm³", "260 KS"),
                ("1.6 MZR-CD", "Dizel", "1.560 cm³", "109 KS"),
                ("2.2 MZR-CD", "Dizel", "2.184 cm³", "150–185 KS"),
             ]),
            ("3. generacija (BM/BN)", "2013–2019", "Hečbek s pet vrata i limuzina.",
             "mazda3-bm.webp", [
                ("1.5 Skyactiv-G", "Benzin", "1.496 cm³", "100–120 KS"),
                ("2.0 Skyactiv-G", "Benzin", "1.998 cm³", "120–165 KS"),
                ("1.5 Skyactiv-D", "Dizel", "1.499 cm³", "105 KS"),
                ("2.2 Skyactiv-D", "Dizel", "2.191 cm³", "150 KS"),
             ]),
            ("4. generacija (BP)", "2019–danas", "Hečbek s pet vrata i limuzina.",
             "mazda3-bp.webp", [
                ("2.0 e-Skyactiv G", "Benzin (MHEV)", "1.998 cm³", "122 KS"),
                ("2.0 e-Skyactiv X", "Benzin (MHEV)", "1.998 cm³", "180–186 KS"),
                ("1.8 Skyactiv-D", "Dizel", "1.759 cm³", "116 KS"),
             ]),
        ],
        "photo_credit": ('Fotografije generacija: Wikimedia Commons — '
                         'Vauxford (CC BY-SA 4.0), Kārlis Dambrāns (CC BY 2.0) i javno vlasništvo.'),
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora.",
        "service": [
            ("Skyactiv-G benzinci i lanac razvoda",
             "Kod benzinaca proveravamo lanac razvoda, rad ubrizgavanja i po potrebi čistimo usisni trakt i EGR, jer neravnomeran rad najčešće počinje odatle."),
            ("Skyactiv-D dizel i DPF",
             "Kod dizela pratimo regeneraciju i stanje DPF filtera, EGR ventil i sistem ubrizgavanja, česte tačke kod gradske vožnje na kratkim relacijama."),
            ("Trap i kočnice",
             "Proveravamo amortizere, spone i ležajeve, kao i diskove i pločice, jer se na Mazdi 3 najviše troše u svakodnevnoj vožnji."),
            ("Elektrika i klima",
             "Kontrolišemo alternator, akumulator i punjenje klime, uz proveru multimedije i senzora kod novijih generacija."),
        ],
    },
    "mazda-6.html": {
        "name": "Mazda 6",
        "title": "Servis za Mazdu 6 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za sve generacije Mazde 6 (GG/GY, GH, GJ/GL) u Beogradu. MZR benzinci, Skyactiv-G i Skyactiv-D motori, lanac razvoda, DPF i pregled pre kupovine.",
        "lead": "Servisiramo sve generacije Mazde 6, od prvih MZR benzinaca i dizela do Skyactiv-G i Skyactiv-D motora.",
        "photo": "mazda6-dimenzije.webp",
        "diagram": True,
        "photo_alt": "Dimenzije i proporcije modela Mazda 6 (tehnički crtež)",
        "intro": ('<p class="lead">Mazda 6 je porodična limuzina i karavan koji vozači biraju zbog prostora, udobnosti i pouzdanih motora. '
                  'Kroz našu radionicu prošle su sve tri generacije, pa svaku dobro poznajemo.</p>'
                  '<p class="muted">Radimo od starijih MZR benzinaca i dizela do Skyactiv-G i Skyactiv-D motora. '
                  'Redovan servis, dijagnostiku Mazda opremom i popravke pratimo pisanim izveštajem o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (GG/GY)", "2002–2008", "Limuzina, hečbek i karavan.",
             "mazda6-gg.webp", [
                ("1.8 MZR", "Benzin", "1.798 cm³", "120 KS"),
                ("2.0 MZR", "Benzin", "1.999 cm³", "141–147 KS"),
                ("2.3 MZR", "Benzin", "2.261 cm³", "166 KS"),
                ("2.3 DISI Turbo (MPS)", "Benzin", "2.261 cm³", "260 KS"),
                ("2.0 MZR-CD", "Dizel", "1.998 cm³", "121–143 KS"),
             ]),
            ("2. generacija (GH)", "2008–2012", "Limuzina, hečbek i karavan.",
             "mazda6-gh.webp", [
                ("1.8 MZR", "Benzin", "1.798 cm³", "120 KS"),
                ("2.0 MZR", "Benzin", "1.999 cm³", "147–155 KS"),
                ("2.5 MZR", "Benzin", "2.488 cm³", "170 KS"),
                ("2.0 MZR-CD", "Dizel", "1.998 cm³", "121–140 KS"),
                ("2.2 MZR-CD", "Dizel", "2.184 cm³", "129–180 KS"),
             ]),
            ("3. generacija (GJ/GL)", "2012–2024", "Limuzina i karavan. Kroz proizvodnju je dva puta redizajnirana (2015. i 2018).",
             "mazda6-gj.webp", [
                ("2.0 Skyactiv-G", "Benzin", "1.998 cm³", "145–165 KS"),
                ("2.5 Skyactiv-G", "Benzin", "2.488 cm³", "192–194 KS"),
                ("2.2 Skyactiv-D", "Dizel", "2.191 cm³", "150–184 KS"),
             ], [
                ("Redizajn 2015", "mazda6-gj-2015.webp"),
                ("Redizajn 2018", "mazda6-gj-2018.webp"),
             ]),
        ],
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora.",
        "photo_credit": ('Fotografije generacija: Wikimedia Commons — '
                         'Vauxford i Alexander-93 (CC BY-SA 4.0), M 93 (CC BY-SA 3.0 DE) i RL GNZLZ (CC BY-SA 2.0).'),
        "service": [
            ("MZR benzinci i lanac razvoda",
             "Kod starijih MZR benzinaca proveravamo lanac razvoda, bobine i svećice, jer neravnomeran rad motora najčešće počinje odatle."),
            ("Skyactiv-D dizel i DPF",
             "Kod dizela pratimo regeneraciju i stanje DPF filtera, EGR ventil i sistem ubrizgavanja, česte tačke kod autoputa i gradske vožnje na kratkim relacijama."),
            ("Trap i kočnice",
             "Kod limuzine i karavana proveravamo amortizere, spone i ležajeve, kao i diskove i pločice, jer veći auto više opterećuje trap."),
            ("Elektrika i klima",
             "Kontrolišemo alternator, akumulator i punjenje klime, uz proveru multimedije i senzora kod novijih generacija."),
        ],
    },
    "cx-3.html": {
        "name": "CX-3",
        "title": "Servis za Mazdu CX-3 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za Mazdu CX-3 (DK) u Beogradu. Skyactiv-G benzinci i Skyactiv-D dizeli, i-Activ AWD, DPF i pregled pre kupovine.",
        "lead": "Servisiramo Mazdu CX-3, kompaktni gradski krosover sa Skyactiv-G i Skyactiv-D motorima.",
        "photo": "cx3-side.webp",
        "diagram": True,
        "photo_alt": "Mazda CX-3 — bočni izgled",
        "intro": ('<p class="lead">Mazda CX-3 je kompaktni krosover baziran na platformi Mazde 2, popularan zbog povišene pozicije za vožnju, kompaktnih dimenzija i niske potrošnje. '
                  'Kroz našu radionicu prošlo je dosta ovih vozila, pa model dobro poznajemo.</p>'
                  '<p class="muted">Radimo Skyactiv-G benzince i Skyactiv-D dizele, uključujući i-Activ AWD verzije sa pogonom na sve točkove. '
                  'Redovan servis, dijagnostiku Mazda opremom i popravke pratimo pisanim izveštajem o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (DK)", "2015–2021", "Kompaktni krosover (SUV), FWD i i-Activ AWD. Redizajniran 2018. (osvežena maska, oprema i šasija).",
             "cx3-dk.webp", [
                ("2.0 Skyactiv-G", "Benzin", "1.998 cm³", "120–121 KS"),
                ("1.5 Skyactiv-D", "Dizel", "1.499 cm³", "105 KS"),
                ("1.8 Skyactiv-D", "Dizel", "1.759 cm³", "115 KS"),
             ], [
                ("Redizajn 2018", "cx3-2018.webp"),
             ]),
        ],
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora. Dizel 1.5 (2015–2018), 1.8 (2018–2021).",
        "photo_credit": "Fotografije: Wikimedia Commons — Vauxford (CC BY-SA 4.0).",
        "service": [
            ("Skyactiv-G benzinci i lanac razvoda",
             "Kod benzinaca proveravamo lanac razvoda, rad ubrizgavanja i po potrebi čistimo usisni trakt i EGR, jer neravnomeran rad najčešće počinje odatle."),
            ("Skyactiv-D dizel i DPF",
             "Kod dizela pratimo regeneraciju i stanje DPF filtera, EGR ventil i sistem ubrizgavanja, česte tačke kod gradske vožnje na kratkim relacijama."),
            ("Trap, kočnice i AWD",
             "Proveravamo amortizere, spone i ležajeve, diskove i pločice, a kod i-Activ AWD verzija i stanje zadnjeg diferencijala i kardana."),
            ("Elektrika i klima",
             "Kontrolišemo alternator, akumulator i punjenje klime, uz proveru multimedije i senzora asistencije."),
        ],
    },
    "cx-30.html": {
        "name": "CX-30",
        "title": "Servis za Mazdu CX-30 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za Mazdu CX-30 (DM) u Beogradu. Skyactiv-G i Skyactiv-X benzinci, Skyactiv-D dizel, i-Activ AWD, blaga hibridna podrška i pregled pre kupovine.",
        "lead": "Servisiramo Mazdu CX-30, kompaktni krosover sa Skyactiv-G, Skyactiv-X i Skyactiv-D motorima.",
        "photo": "cx30-dimenzije.webp",
        "diagram": True,
        "photo_alt": "Dimenzije i proporcije modela Mazda CX-30 (tehnički crtež)",
        "intro": ('<p class="lead">Mazda CX-30 je kompaktni krosover baziran na platformi Mazde 3, sa nešto povišenom pozicijom, kvalitetnom kabinom i modernim Skyactiv motorima. '
                  'Novijeg je datuma, ali smo već dobro upoznati sa njegovim održavanjem.</p>'
                  '<p class="muted">Radimo Skyactiv-G i Skyactiv-X benzince sa blagom hibridnom podrškom i Skyactiv-D dizel, uključujući i-Activ AWD verzije. '
                  'Redovan servis, dijagnostiku Mazda opremom i popravke pratimo pisanim izveštajem o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (DM)", "2019–danas", "Kompaktni krosover (SUV), FWD i i-Activ AWD, uz blagu hibridnu podršku (M Hybrid).",
             "cx30-dm.webp", [
                ("2.0 e-Skyactiv G (M Hybrid)", "Benzin (MHEV)", "1.998 cm³", "122–150 KS"),
                ("2.0 e-Skyactiv X (M Hybrid)", "Benzin (MHEV)", "1.998 cm³", "180–186 KS"),
                ("1.8 Skyactiv-D", "Dizel", "1.759 cm³", "116 KS"),
             ]),
        ],
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora.",
        "photo_credit": "Fotografije: Wikimedia Commons — EurovisionNim (CC BY-SA 4.0).",
        "service": [
            ("Skyactiv-G / Skyactiv-X benzinci",
             "Kod benzinaca proveravamo lanac razvoda, rad ubrizgavanja i mild-hybrid sistem (24V), a kod Skyactiv-X i rad SPCCI paljenja i senzore pritiska."),
            ("Skyactiv-D dizel i DPF",
             "Kod dizela pratimo regeneraciju i stanje DPF filtera, EGR ventil i sistem ubrizgavanja, česte tačke kod gradske vožnje na kratkim relacijama."),
            ("Trap, kočnice i AWD",
             "Proveravamo amortizere, spone i ležajeve, diskove i pločice, a kod i-Activ AWD verzija i stanje zadnjeg diferencijala i kardana."),
            ("Elektrika i klima",
             "Kontrolišemo alternator, akumulator i punjenje klime, uz proveru multimedije i sistema asistencije vozaču."),
        ],
    },
    "cx-5.html": {
        "name": "CX-5",
        "title": "Servis za Mazdu CX-5 | EAST Auto Servis",
        "desc": "Servis, dijagnostika i popravke za sve generacije Mazde CX-5 (KE, KF) u Beogradu. Skyactiv-G benzinci i Skyactiv-D dizeli, DPF, i-Activ AWD i pregled pre kupovine.",
        "lead": "Servisiramo obe generacije Mazde CX-5, sa Skyactiv-G benzincima i Skyactiv-D dizelima.",
        "photo": "cx5-dimenzije.webp",
        "diagram": True,
        "photo_alt": "Dimenzije i proporcije modela Mazda CX-5 (tehnički crtež)",
        "intro": ('<p class="lead">Mazda CX-5 je najprodavaniji Mazdin krosover i čest gost naše radionice, posebno dizel verzije. '
                  'Prošle su kroz nas obe generacije, pa ih dobro poznajemo.</p>'
                  '<p class="muted">Radimo Skyactiv-G benzince i Skyactiv-D dizele, uključujući i-Activ AWD verzije sa pogonom na sve točkove. '
                  'Redovan servis, dijagnostiku Mazda opremom i popravke pratimo pisanim izveštajem o stanju vozila posle svake intervencije.</p>'),
        "gens": [
            ("1. generacija (KE)", "2012–2017", "Kompaktni krosover (SUV), FWD i i-Activ AWD. Redizajniran 2015.",
             "cx5-ke.webp", [
                ("2.0 Skyactiv-G", "Benzin", "1.998 cm³", "160–165 KS"),
                ("2.2 Skyactiv-D", "Dizel", "2.191 cm³", "150–175 KS"),
             ]),
            ("2. generacija (KF)", "2017–danas", "Kompaktni krosover (SUV), FWD i i-Activ AWD. Redizajniran 2021.",
             "cx5-kf.webp", [
                ("2.0 Skyactiv-G", "Benzin", "1.998 cm³", "165 KS"),
                ("2.5 Skyactiv-G", "Benzin", "2.488 cm³", "194 KS"),
                ("2.2 Skyactiv-D", "Dizel", "2.191 cm³", "150–184 KS"),
             ]),
        ],
        "engines_note": "EU/RS ponuda motora. Snaga je okvirna, po verziji motora. Od 2022. 2.0 i 2.2 (KF) dobijaju blagu hibridnu podršku (M Hybrid).",
        "photo_credit": "Fotografije generacija: Wikimedia Commons — M 93 (CC BY-SA 3.0 DE) i Tokumeigakarinoaoshima (CC0, javno vlasništvo).",
        "service": [
            ("Skyactiv-D dizel i DPF",
             "CX-5 je najčešće dizel; pratimo regeneraciju i stanje DPF filtera, EGR ventil i sistem ubrizgavanja, česte tačke kod gradske vožnje na kratkim relacijama."),
            ("Skyactiv-G benzinci i lanac razvoda",
             "Kod benzinaca proveravamo lanac razvoda, rad ubrizgavanja i po potrebi čistimo usisni trakt i EGR, jer neravnomeran rad najčešće počinje odatle."),
            ("Trap, kočnice i AWD",
             "Proveravamo amortizere, spone i ležajeve, diskove i pločice, a kod i-Activ AWD verzija i stanje zadnjeg diferencijala i kardana."),
            ("Elektrika i klima",
             "Kontrolišemo alternator, akumulator i punjenje klime, uz proveru multimedije i sistema asistencije vozaču."),
        ],
    },
}


def gen_engine_table(engines):
    rows = []
    for motor, fuel, disp, power in engines:
        fuel_cls = "is-diesel" if "Dizel" in fuel else "is-petrol"
        rows.append(
            f'            <tr><td class="etbl-motor">{motor}</td>'
            f'<td><span class="etbl-fuel {fuel_cls}">{fuel}</span></td>'
            f'<td class="etbl-num">{disp}</td>'
            f'<td class="etbl-num">{power}</td></tr>')
    body = "\n".join(rows)
    return f"""        <div class="etbl-wrap">
          <table class="etbl gen-etbl">
            <thead>
              <tr><th scope="col">Motor</th><th scope="col">Gorivo</th><th scope="col">Zapremina</th><th scope="col">Snaga</th></tr>
            </thead>
            <tbody>
{body}
            </tbody>
          </table>
        </div>"""


def gen_cards(gens, model_name):
    cards = []
    for g in gens:
        # Novi format: (naziv, godine, karoserija, foto, [motori][, [redizajni]]) → foto + tabela motora
        if len(g) >= 5 and isinstance(g[4], list):
            title, years, body, photo, engines = g[:5]
            facelifts = g[5] if len(g) > 5 else None
            pic = (f'<img class="gen-photo" src="img/modeli/{photo}" alt="{title} modela {model_name}" loading="lazy">'
                   if photo else "")
            block_cls = "gen-block" if photo else "gen-block is-noimg"
            fl = ""
            if facelifts:
                figs = "\n".join(
                    f'            <figure><img src="img/modeli/{fp}" alt="{model_name} {cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
                    for cap, fp in facelifts)
                fl = ('          <p class="gen-facelifts-lead">Redizajni tokom proizvodnje:</p>\n'
                      '          <div class="gen-facelifts">\n' + figs + '\n          </div>\n')
            cards.append(
                f'      <li class="{block_cls}">{pic}\n'
                f'        <div class="gen-body">\n'
                f'          <h3 class="h3">{title} · {years}</h3>\n'
                f'          <p>{body}</p>\n'
                f'{gen_engine_table(engines)}\n'
                f'{fl}'
                f'        </div></li>')
        else:
            # Stari format: (naziv, godine, karoserija, motori-proza[, foto])
            title, years, body, engines = g[:4]
            photo = g[4] if len(g) > 4 else None
            pic = (f'<img class="gen-photo" src="img/modeli/{photo}" alt="{title} modela {model_name}" loading="lazy">'
                   if photo else "")
            cards.append(f'      <li>{pic}<h3 class="h3">{title} · {years}</h3><p>{body} {engines}</p></li>')
    return "\n".join(cards)


def service_cards(items):
    return "\n".join(
        f'      <li><h3 class="h3">{h}</h3><p>{p}</p></li>' for h, p in items)


def cert_section(slug, m):
    certs = AUTO_CERTS.get(slug)
    if not certs:
        return ""
    cards = "\n".join(
        f'      <a href="img/sertifikati/{fn}" data-lb="cert" data-caption="{cap}">'
        f'<img src="img/sertifikati/mala/{fn}" alt="{cap}" loading="lazy"></a>'
        for fn, cap in certs)
    return f"""
<section class="section section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Sertifikati za {m['name']}</h2>
      <p>Mazda obuke i modelski treninzi koje su naši mehaničari prošli za ovaj model. Kliknite na sertifikat za punu veličinu.</p>
    </div>
    <div class="thumb-grid certs">
{cards}
    </div>
  </div>
</section>
"""


def model_page(slug, m):
    diagram = m.get("diagram")
    img_cls = "model-photo is-diagram" if diagram else "model-photo"
    img_dir = m.get("photo_dir") or ("img/modeli/" if diagram else "img/galerija/")
    default_alt = f"Dimenzije modela {m['name']}" if diagram else f"{m['name']} u servisu EAST Auto Servis"
    img_alt = m.get("photo_alt", default_alt)
    blueprint = (f'\n      <img class="model-blueprint" src="img/modeli/{m["blueprint"]}" '
                 f'alt="Tehnički crtež modela {m["name"]} sa merama" loading="lazy">' if m.get("blueprint") else "")
    has_engine_tables = any(len(g) >= 5 and isinstance(g[4], list) for g in m['gens'])
    gen_head = "Generacije i motori" if has_engine_tables else "Generacije koje servisiramo"
    gen_sub = (f"Radimo sve generacije modela {m['name']} zastupljene na našem tržištu, sa fabričkim varijantama motora uz svaku."
               if has_engine_tables
               else f"Radimo sve generacije modela {m['name']} zastupljene na našem tržištu.")
    gen_ul_cls = "gen-list" if has_engine_tables else "service-list"
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
      <h2 class="h2">{gen_head}</h2>
      <p>{gen_sub}</p>
    </div>
    <ul class="{gen_ul_cls}">
{gen_cards(m['gens'], m['name'])}
    </ul>{f'''
    <p class="photo-credit">{m["engines_note"]}</p>''' if m.get("engines_note") else ""}{f'''
    <p class="photo-credit">{m["photo_credit"]}</p>''' if m.get("photo_credit") else ""}
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
{cert_section(slug, m)}""" + CTA + foot(lightbox=bool(AUTO_CERTS.get(slug)))
    write(slug, html)


# ---------------- SERTIFIKATI: obrada + raspoređivanje ----------------
# Originali su u ../sertifikati/ (van projekta). Svaki je pročitan i ručno mapiran:
#   "models"  -> strane modela na kojima se prikazuje (model-specifičan trening)
#   "engine"  -> "diesel"/"petrol": dodaje se na SVE strane modela koje imaju taj motor
#   "general" -> True: opšta obuka (elektrika/kočnice), samo na glavnoj strani Sertifikati
# Glavna strana sertifikati.html prikazuje SVE (redosled = CERTS, hronološki). Slug = ime webp.
try:
    from PIL import Image as _CImage
    _HAS_PIL = True
except Exception:
    _HAS_PIL = False

CERT_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sertifikati")
CERT_DIR = "img/sertifikati"
CERT_THUMB = os.path.join(CERT_DIR, "mala")

CERTS = [
    {"src": "Mazda6-GG-MPV-LW.jpeg", "slug": "mazda6-gg-2002",
     "cap": "Mazda 6 (GG) i MPV (LW) — modelski trening, 2002.", "models": ["mazda-6.html"]},
    {"src": "Sertifikat_02.jpeg", "slug": "rx8-se-2004",
     "cap": "RX-8 (SE) — modelski trening, 2004.", "models": []},
    {"src": "Sertifikat_03.jpeg", "slug": "dizel-edc-2004",
     "cap": "Elektronska dizel regulacija (EDC) — 2004.", "engine": "diesel"},
    {"src": "Sertifikat_04.jpeg", "slug": "mazda5-cr-2005",
     "cap": "Mazda 5 (CR) — modelski trening, 2005.", "models": []},
    {"src": "Sertifikat_05.jpeg", "slug": "dizel-common-rail-dpf-2006",
     "cap": "Common Rail dizel sa DPF — 2006.", "engine": "diesel"},
    {"src": "Sertifikat_06.jpeg", "slug": "elektrika-1-2006",
     "cap": "Elektrika 1 — 2006.", "general": True},
    {"src": "Sertifikat_07.jpeg", "slug": "mx5-rc-2007",
     "cap": "MX-5 (RC) — modelski trening, 2007.", "models": []},
    {"src": "Sertifikat_08.jpeg", "slug": "mazda2-cx7-2007",
     "cap": "Mazda 2 i CX-7 — modelski trening, 2007.", "models": ["mazda-2.html"]},
    {"src": "Sertifikat_09.jpeg", "slug": "mazda6-gh-2008",
     "cap": "Mazda 6 (GH) i Mazda 5 (CR) — modelski trening, 2008.", "models": ["mazda-6.html"]},
    {"src": "Sertifikat_10.jpeg", "slug": "benzin-ubrizgavanje-2008",
     "cap": "Elektronsko benzinsko ubrizgavanje — 2008.", "engine": "petrol"},
    {"src": "Sertifikat_11.jpeg", "slug": "kocnice-abs-dsc-2008",
     "cap": "Kočnice — ABS/DSC — 2008.", "general": True},
    {"src": "Sertifikat_12.jpeg", "slug": "dizel-regulacija-2008",
     "cap": "Elektronska dizel regulacija — 2008.", "engine": "diesel"},
    {"src": "Sertifikat_13.jpeg", "slug": "mazda6-gh-22-dizel-2009",
     "cap": "Mazda 6 (GH) 2.2 dizel motor — 2009.", "models": ["mazda-6.html"]},
    {"src": "Sertifikat_14.jpeg", "slug": "dizel-management-2010",
     "cap": "Dizel motor — upravljanje i dijagnostika — 2010.", "engine": "diesel"},
    {"src": "Sertifikat_15.jpeg", "slug": "cx5-skyactiv-2012",
     "cap": "CX-5 sa Skyactiv tehnologijom — 2012.", "models": ["cx-5.html"]},
]


def _convert_cert(src, slug):
    path = os.path.join(CERT_SRC, src)
    out_full = os.path.join(CERT_DIR, slug + ".webp")
    out_thumb = os.path.join(CERT_THUMB, slug + ".webp")
    if not (_HAS_PIL and os.path.exists(path)):
        return
    if os.path.exists(out_full) and os.path.getmtime(path) <= os.path.getmtime(out_full):
        return
    im = _CImage.open(path).convert("RGB")
    w, h = im.size
    fw = min(1100, w)
    im.resize((fw, round(h * fw / w)), _CImage.LANCZOS).save(out_full, "WEBP", quality=85, method=6)
    tw = 380
    im.resize((tw, round(h * tw / w)), _CImage.LANCZOS).save(out_thumb, "WEBP", quality=82, method=6)


def _model_engine_kinds(page):
    kinds = set()
    for g in MODELS.get(page, {}).get("gens", []):
        if len(g) >= 5 and isinstance(g[4], list):
            for eng in g[4]:
                fuel = eng[1]
                if "Dizel" in fuel:
                    kinds.add("diesel")
                if "Benzin" in fuel:
                    kinds.add("petrol")
    return kinds


def build_certs():
    os.makedirs(CERT_THUMB, exist_ok=True)
    for c in CERTS:
        _convert_cert(c["src"], c["slug"])
    all_list = [(c["slug"] + ".webp", c["cap"]) for c in CERTS]
    per_model = {}
    for page in MODELS:
        kinds = _model_engine_kinds(page)
        model_specific = [(c["slug"] + ".webp", c["cap"]) for c in CERTS if page in c.get("models", [])]
        engine_certs = [(c["slug"] + ".webp", c["cap"]) for c in CERTS if c.get("engine") in kinds]
        combined = model_specific + engine_certs
        if combined:
            per_model[page] = combined
    print(f"Sertifikati: {len(all_list)} ukupno; po modelu "
          + ", ".join(f"{p}={len(v)}" for p, v in per_model.items()))
    return per_model, all_list


AUTO_CERTS, ALL_CERTS = build_certs()


for _slug, _m in MODELS.items():
    model_page(_slug, _m)

# Samostalna strana „Sertifikati" je uklonjena — sertifikati se prikazuju
# samo na stranama modela (cert_section, po modelu/tipu motora).

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
             "EAST Auto Servis je otvoren 2000. godine kao specijalizovani Mazda servis u Beogradu. Sertifikovani mehaničari i više od 1500 stalnih klijenata.",
             "o-nama.html") + page_head("O nama",
             "Otvorili smo servis 2000. sa jednom idejom: da radimo samo Mazde i da ih radimo kako treba.") + f"""
<section class="section">
  <div class="wrap split">
    <div>
      <h2 class="h2">Ko smo mi</h2>
    </div>
    <div class="measure">
      <p class="lead">EAST Auto Servis je specijalizovan za vozila marke Mazda. Naši mehaničari imaju višegodišnje iskustvo i međunarodne Mazda sertifikate.</p>
      <p class="muted">Stalno ulaganje u opremu i obuku omogućilo nam je da danas imamo više od 1500 klijenata koji nam se vraćaju. Kod nas možete kompletno održavati svoje vozilo ili ceo vozni park: od automehanike i dijagnostike do popravki.</p>
      <img class="photo-wide mt" src="{IMG}galerija/Servis_mazda_dijagnostika_01.jpg" alt="Mazda na dijagnostici u radionici" loading="lazy">
    </div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    <div class="section-head"><h2 class="h2">Kako smo rasli</h2></div>
    <ol class="timeline">
      <li><span class="year">2000</span><div><h3 class="h3">Otvaranje servisa</h3><p>Počinjemo kao servis specijalizovan isključivo za Mazda vozila.</p></div></li>
      <li><span class="year">2012</span><div><h3 class="h3">Proširenje radionice</h3><p>Servis dobija više radnih mesta, svako kompletno opremljeno potrebnim alatom.</p></div></li>
      <li><span class="year">Danas</span><div><h3 class="h3">Više od 1500 stalnih klijenata</h3><p>Petnaest Mazda sertifikata, savremena dijagnostika i klijenti koji nam poveravaju i svoje vozne parkove.</p></div></li>
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
        <div class="info-block"><h2>Društvene mreže</h2>{SOCIAL}</div>
      </aside>
    </div>
    <div class="map-full"><iframe src="{MAP}" title="Lokacija servisa na mapi" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
""" + foot()
write("kontakt.html", kontakt)

print("Generisano:", ", ".join(p for p, _ in PAGES))
