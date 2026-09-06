# -*- coding: utf-8 -*-
"""Bouwt margrietbloemdecoraties.nl naar dist/."""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sitegen
import theme
import layout
import content_inhuis as inhuis
import content_stijl as stijl
import content_oplocatie as oplocatie
import content_onderhoud as onderhoud
import content_journaal as journaal

BASIS = layout.BASIS
NAAM = layout.NAAM
MAIL = layout.MAIL
sitegen.SITE["gewijzigd"] = "2026-09-06"

RUBRIEKEN = [inhuis, stijl, oplocatie, onderhoud]
MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus",
           "september", "oktober", "november", "december"]


def datumtekst(datum):
    j, m, d = datum.split("-")
    return "%d %s %s" % (int(d), MAANDEN[int(m) - 1], j)


def url_van(mod, p):
    return mod.RUBRIEK["url"] + p["slug"] + "/"


def indexlijst(mod, paginas=None):
    rijen = []
    for n, p in enumerate(paginas or mod.PAGINAS, start=1):
        rijen.append('<li><a href="%s"><span class="nr">%02d</span>'
                     '<span class="titel">%s</span><span class="toe">%s</span></a></li>'
                     % (url_van(mod, p), n, html.escape(p["titel"]), html.escape(p["kaart"])))
    return '<ul class="index">%s</ul>' % "".join(rijen)


def journaallijst(paginas):
    rijen = "".join(
        '<li><a href="%s"><span class="dat">%s</span><span class="kop">%s</span></a></li>'
        % (url_van(journaal, p), datumtekst(p["datum"]), html.escape(p["titel"]))
        for p in paginas)
    return '<ul class="journaal">%s</ul>' % rijen


def gesorteerd():
    return sorted(journaal.PAGINAS, key=lambda p: p["datum"], reverse=True)


def winkelblok(winkel):
    if not winkel:
        return ""
    kop, tekst = winkel
    return ('<div class="winkel"><h2>%s</h2>%s</div>'
            % (html.escape(kop), sitegen.markdown(tekst)))


def artikelpagina(mod, p):
    url = url_van(mod, p)
    koppen = []
    romp = sitegen.markdown(p["body"], koppen)
    zij = ""
    if len(koppen) >= 3:
        zij = ('<aside class="zij"><p class="label">Op deze pagina</p><ol>%s</ol></aside>'
               % "".join('<li><a href="#%s">%s</a></li>' % (s, html.escape(t))
                         for s, t in koppen))
    ander = [q for q in mod.PAGINAS if q["slug"] != p["slug"]][:4]
    verder = ('<h2>Verder in %s</h2>%s'
              % (html.escape(mod.RUBRIEK["h1"].lower()), journaalachtig(mod, ander)))
    artikel = ('<article><h1>%s</h1>%s<p class="lood">%s</p>%s%s%s</article>'
               % (html.escape(p["titel"]),
                  '<p class="label">%s</p>' % datumtekst(p["datum"]) if p.get("datum") else "",
                  html.escape(p["lood"]), romp, winkelblok(p.get("winkel")), verder))
    inhoud = '<div class="wrap"><div class="kolommen">%s%s</div></div>' % (zij, artikel)
    meta = {"url": url,
            "titel": p["titel"] + " | " + NAAM if len(p["titel"]) <= 42 else p["titel"],
            "omschrijving": p["omschrijving"],
            "kruimel": [(mod.RUBRIEK["url"], mod.RUBRIEK["h1"]), (url, p["titel"])]}
    if p.get("datum"):
        meta["datum"] = p["datum"]
    return meta, inhoud


def journaalachtig(mod, paginas):
    rijen = "".join(
        '<li><a href="%s"><span class="dat">%s</span><span class="kop">%s</span></a></li>'
        % (url_van(mod, p), html.escape(p["kaart"]), html.escape(p["titel"]))
        for p in paginas)
    return '<ul class="journaal">%s</ul>' % rijen


def rubriekpagina(mod):
    r = mod.RUBRIEK
    inhoud = ('<div class="wrap"><section class="blok"><p class="label">%s</p>'
              '<h1>%s</h1><p class="lood">%s</p>%s</section></div>'
              % (html.escape(NAAM), html.escape(r["h1"]), html.escape(r["lood"]),
                 indexlijst(mod)))
    meta = {"url": r["url"], "titel": r["titel"], "omschrijving": r["omschrijving"],
            "kruimel": [(r["url"], r["h1"])]}
    return meta, inhoud


def journaalpagina():
    r = journaal.RUBRIEK
    inhoud = ('<div class="wrap"><section class="blok"><p class="label">%s</p>'
              '<h1>%s</h1><p class="lood">%s</p>%s'
              '<p style="margin-top:26px"><a href="/feed.xml">Rss-feed van het journaal</a></p>'
              "</section></div>"
              % (html.escape(NAAM), html.escape(r["h1"]), html.escape(r["lood"]),
                 journaallijst(gesorteerd())))
    meta = {"url": r["url"], "titel": r["titel"], "omschrijving": r["omschrijving"],
            "kruimel": [(r["url"], r["h1"])]}
    return meta, inhoud


PRINCIPES = [
    ("Verhouding eerst",
     "Een stuk klopt door de verhouding tussen vaas, bloemen en meubel. Kleur is de laatste "
     "stap, niet de eerste."),
    ("De plek bepaalt de vorm",
     "Op een eettafel laag, in een hal hoog en smal, voor een raam met een duidelijk "
     "silhouet. De ruimte schrijft de vorm voor."),
    ("Onderhoud is een keuze vooraf",
     "Wat wekelijks verzorging vraagt, blijft alleen staan waar iemand die tijd heeft. "
     "Elders houdt blijvend materiaal het beeld overeind."),
]


def home():
    principes = "".join(
        '<div><p class="nr">%02d</p><h3>%s</h3><p>%s</p></div>' % (n, html.escape(k),
                                                                   html.escape(t))
        for n, (k, t) in enumerate(PRINCIPES, start=1))
    inhoud = """
<section class="opening"><div class="wrap">
<div>
<p class="label">Bloemdecoratie in huis en op locatie</p>
<h1>Waar een bloemstuk staat, bepaalt hoe het eruit hoort te zien</h1>
<div class="streep"></div>
<p class="lood">Per ruimte een andere hoogte, per licht een andere kleur, per gebruik een
ander materiaal. Deze site behandelt bloemdecoratie als een kwestie van verhouding en
plaatsing, niet van smaak.</p>
</div>
%(held)s
</div></section>

<div class="wrap"><section class="blok">
<p class="label">Per ruimte</p>
<h2>In huis</h2>
%(inhuis)s
</section></div>

<section class="band"><div class="wrap">
<p class="label">Drie uitgangspunten</p>
<div class="principes">%(principes)s</div>
</div></section>

<div class="wrap"><section class="blok">
<p class="label">Opbouw en verhouding</p>
<h2>Stijl</h2>
%(stijl)s
</section></div>

<div class="wrap"><section class="blok lijn">
<p class="label">Buiten de woning</p>
<h2>Op locatie</h2>
%(oplocatie)s
</section></div>

<div class="wrap"><section class="blok lijn">
<p class="label">Journaal</p>
<h2>Laatste artikelen</h2>
%(journaal)s
<p style="margin-top:22px"><a href="/journaal/">Alle artikelen in het journaal</a></p>
</section></div>

<div class="wrap">
<div class="winkel">
<h2>Blijvende bloemen en vazen</h2>
<p>Voor decoratie die zonder water blijft staan, levert
<a class="uit" href="https://bloomzy.nl/" rel="nofollow noopener" target="_blank">Bloomzy.nl</a>
zijden boeketten, kunstboeketten, droogboeketten en vazen in beperkte oplage. De collectie
staat op
<a class="uit" href="https://bloomzy.nl/collectie" rel="nofollow noopener" target="_blank">https://bloomzy.nl/collectie</a>.</p>
</div>
</div>
""" % {"held": theme.HELD_SVG, "inhuis": indexlijst(inhuis),
       "principes": principes, "stijl": indexlijst(stijl),
       "oplocatie": indexlijst(oplocatie),
       "journaal": journaallijst(gesorteerd()[:4])}
    meta = {"url": "/", "titel": "Bloemdecoratie in huis en op locatie | " + NAAM,
            "omschrijving": "Redactionele gids over bloemdecoratie: welke bloemen waar "
                            "staan, in welke vaas, in welke verhouding en met welk "
                            "onderhoud."}
    return meta, inhoud


def tekstpagina(url, titel, oms, h1, lood, body, noindex=False):
    koppen = []
    romp = sitegen.markdown(body, koppen)
    zij = ""
    if len(koppen) >= 3:
        zij = ('<aside class="zij"><p class="label">Op deze pagina</p><ol>%s</ol></aside>'
               % "".join('<li><a href="#%s">%s</a></li>' % (s, html.escape(t))
                         for s, t in koppen))
    inhoud = ('<div class="wrap"><div class="kolommen">%s<article><h1>%s</h1>'
              '<p class="lood">%s</p>%s</article></div></div>'
              % (zij, html.escape(h1), html.escape(lood), romp))
    meta = {"url": url, "titel": titel, "omschrijving": oms,
            "kruimel": [(url, h1)]}
    if noindex:
        meta["noindex"] = True
    return meta, inhoud


def vaste_paginas():
    uit = []
    uit.append(tekstpagina(
        "/over/", "Over deze site | " + NAAM,
        "Wat Margriet Bloemdecoraties behandelt, hoe de teksten tot stand komen en waar de "
        "verwijzingen naartoe gaan.",
        "Over deze site",
        "Margriet Bloemdecoraties is een Nederlandstalige gids over bloemdecoratie in huis "
        "en op locatie.",
        """
## Wat hier staat

De site behandelt vier onderwerpen: de plek van een bloemstuk per ruimte, de opbouw en
verhouding van een stuk, decoratie buiten de woning en het onderhoud van blijvend
materiaal. Daarnaast staat er een journaal met achtergrondartikelen.

## Uitgangspunt

Bloemdecoratie wordt hier behandeld als een kwestie van verhouding, licht en gebruik. Wat
op een foto mooi is, hoeft in een ruimte niet te kloppen. De teksten gaan daarom over
hoogte, plaatsing en materiaal, en pas daarna over kleur.

## Hoe de teksten tot stand komen

De informatie komt uit de praktijk van bloembinden en interieurstyling, aangevuld met
openbare informatie van leveranciers over materiaal en onderhoud. Er staan geen prijzen op
deze site, omdat die per seizoen en per aanbieder verschillen.

## Verwijzingen

Op meerdere pagina's staat een verwijzing naar Bloomzy.nl, een Nederlandse webwinkel in
kunstbloemen, zijden boeketten, droogboeketten en vazen. Die verwijzingen staan er omdat
blijvend materiaal in veel van de behandelde situaties de praktische keuze is.

## Contact

Correcties en aanvullingen gaan naar [%(mail)s](mailto:%(mail)s).

## Uitvoering

Voor blijvende boeketten en vazen wordt verwezen naar [Bloomzy.nl](https://bloomzy.nl/).
""" % {"mail": MAIL}))

    uit.append(tekstpagina(
        "/contact/", "Contact | " + NAAM,
        "Contactgegevens van Margriet Bloemdecoraties: correcties, aanvullingen en vragen "
        "over de teksten op deze site.",
        "Contact",
        "Vragen, aanvullingen of correcties op de teksten gaan per e-mail.",
        """
## E-mail

[%(mail)s](mailto:%(mail)s)

Berichten worden op werkdagen gelezen. Er is geen contactformulier en geen telefoonnummer.

## Waarvoor dit adres bedoeld is

- Correcties op de inhoud van een pagina.
- Onderwerpen die ontbreken of aanvulling verdienen.
- Vragen over het gebruik van teksten van deze site.

## Waarvoor niet

Bestellingen, leveringen en klachten over een boeket lopen via de winkel waar de bestelling
is geplaatst. Deze site verkoopt niets.

## Bestellen

Boeketten en vazen staan bij [Bloomzy.nl](https://bloomzy.nl/).
""" % {"mail": MAIL}))

    uit.append(tekstpagina(
        "/privacybeleid/", "Privacybeleid | " + NAAM,
        "Welke gegevens Margriet Bloemdecoraties verwerkt, wat er in de serverlogboeken "
        "staat en welke rechten bezoekers hebben.",
        "Privacybeleid",
        "Deze site verzamelt zo min mogelijk gegevens. Hieronder staat wat er wel en niet "
        "gebeurt.",
        """
## Geen analyse en geen advertenties

Er wordt geen statistiekprogramma gebruikt, geen advertentienetwerk en geen sociale knop.
Bezoekersprofielen worden niet opgebouwd.

## Serverlogboeken

De hostingpartij legt technische gegevens vast die nodig zijn om de site uit te leveren:
ip-adres, tijdstip, opgevraagde pagina en browsertype. Die gegevens dienen voor beveiliging
en storingsonderzoek.

## E-mail

Wie mailt naar %(mail)s deelt daarmee een e-mailadres en de inhoud van het bericht. Die
gegevens worden alleen gebruikt om te antwoorden.

## Externe verwijzingen

Op pagina's staan links naar andere websites, waaronder bloomzy.nl. Na doorklikken geldt
het privacybeleid van die site.

## Rechten

Op grond van de Algemene verordening gegevensbescherming bestaat recht op inzage,
correctie en verwijdering van persoonsgegevens. Een verzoek daartoe kan naar
[%(mail)s](mailto:%(mail)s). Klachten kunnen worden ingediend bij de Autoriteit
Persoonsgegevens.

## Wijzigingen

Wijzigingen verschijnen op deze pagina. Laatste versie: september 2026.
""" % {"mail": MAIL}))

    uit.append(tekstpagina(
        "/cookiebeleid/", "Cookiebeleid | " + NAAM,
        "Margriet Bloemdecoraties plaatst geen cookies en gebruikt geen trackers of "
        "ingesloten inhoud van derden.",
        "Cookiebeleid",
        "Deze site plaatst geen cookies.",
        """
## Geen cookies

Er worden geen cookies geplaatst, ook geen functionele. De site bestaat uit vaste pagina's
zonder inlogfunctie en zonder voorkeuren die bewaard hoeven te worden.

## Geen trackers

Er staat geen statistiekcode, geen advertentiescript en geen ingesloten inhoud van derden
op de pagina's. Tijdens het laden gaat er geen verzoek naar een externe server.

## Wat er wel gebeurt

De browser bewaart pagina's tijdelijk in het eigen geheugen om ze sneller te tonen. Dat is
een browserfunctie en geen cookie.

## Na doorklikken

Wie via een link naar een andere website gaat, komt terecht bij een site met een eigen
cookiebeleid. Webwinkels plaatsen doorgaans wel cookies.

## Vragen

Vragen over dit beleid kunnen naar [%(mail)s](mailto:%(mail)s).
""" % {"mail": MAIL}))
    return uit


def sitemappagina():
    groepen = []
    for mod in RUBRIEKEN + [journaal]:
        links = "".join('<li><a href="%s">%s</a></li>' % (url_van(mod, p),
                                                          html.escape(p["titel"]))
                        for p in mod.PAGINAS)
        groepen.append("<h2>%s</h2><ul>%s</ul>" % (html.escape(mod.RUBRIEK["h1"]), links))
    vast = "".join('<li><a href="%s">%s</a></li>' % (u, n) for u, n in [
        ("/", "Home"), ("/over/", "Over deze site"), ("/contact/", "Contact"),
        ("/privacybeleid/", "Privacybeleid"), ("/cookiebeleid/", "Cookiebeleid")])
    inhoud = ('<div class="wrap"><div class="kolommen"><aside class="zij">'
              '<p class="label">Sitemap</p></aside><article><h1>Sitemap</h1>'
              '<p class="lood">Alle pagina\'s van deze site op een rij.</p>'
              "<h2>Vaste pagina's</h2><ul>%s</ul>%s</article></div></div>"
              % (vast, "".join(groepen)))
    meta = {"url": "/sitemap/", "titel": "Sitemap | " + NAAM,
            "omschrijving": "Overzicht van alle pagina's van Margriet Bloemdecoraties, "
                            "gerangschikt per onderwerp.",
            "kruimel": [("/sitemap/", "Sitemap")]}
    return meta, inhoud


def bouw():
    sitegen.leeg_dist()
    paginas = [home()]
    for mod in RUBRIEKEN:
        paginas.append(rubriekpagina(mod))
        for p in mod.PAGINAS:
            paginas.append(artikelpagina(mod, p))
    paginas.append(journaalpagina())
    for p in journaal.PAGINAS:
        paginas.append(artikelpagina(journaal, p))
    paginas.extend(vaste_paginas())
    paginas.append(sitemappagina())

    for meta, inhoud in paginas:
        sitegen.schrijf_pagina(meta["url"], layout.pagina(meta, inhoud))

    meta404 = {"url": "/404.html", "titel": "Pagina niet gevonden | " + NAAM,
               "omschrijving": "De opgevraagde pagina bestaat niet of is verplaatst. Via "
                               "de sitemap staan alle pagina's op een rij.",
               "noindex": True}
    inhoud404 = ('<div class="wrap"><div class="kolommen"><aside class="zij">'
                 '<p class="label">404</p></aside><article>'
                 "<h1>Pagina niet gevonden</h1>"
                 '<p class="lood">De opgevraagde pagina bestaat niet of is verplaatst.</p>'
                 '<p>Via de <a href="/sitemap/">sitemap</a> staan alle pagina\'s op een rij. '
                 'De rubrieken beginnen bij <a href="/in-huis/">in huis</a>, '
                 '<a href="/stijl/">stijl</a>, <a href="/op-locatie/">op locatie</a> en '
                 '<a href="/onderhoud/">onderhoud</a>.</p></article></div></div>')
    sitegen.schrijf("404.html", layout.pagina(meta404, inhoud404))

    sitegen.schrijf("sitemap.xml", sitegen.sitemap([m for m, _ in paginas], BASIS))
    artikelen = [{"titel": p["titel"], "omschrijving": p["omschrijving"],
                  "url": url_van(journaal, p), "datum": p["datum"]} for p in gesorteerd()]
    sitegen.schrijf("feed.xml", sitegen.rss(artikelen, BASIS, NAAM,
                                            "Journaal van Margriet Bloemdecoraties"))
    sitegen.schrijf("robots.txt",
                    "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASIS)
    sitegen.schrijf("favicon.svg", theme.FAVICON)
    print("paginas:", len(paginas) + 1)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    bouw()
