# -*- coding: utf-8 -*-
"""Sjabloon van margrietbloemdecoraties.nl."""
import html
import json

import theme

BASIS = "https://margrietbloemdecoraties.nl"
NAAM = "Margriet Bloemdecoraties"
CLAIM = "Bloemdecoratie in huis en op locatie, van vaaskeuze tot seizoenswissel"
MAIL = "info@margrietbloemdecoraties.nl"

MENU = [
    ("/in-huis/", "In huis"),
    ("/stijl/", "Stijl"),
    ("/op-locatie/", "Op locatie"),
    ("/onderhoud/", "Onderhoud"),
    ("/journaal/", "Journaal"),
    ("/contact/", "Contact"),
]

VOET = [
    ("Onderwerpen", [("/in-huis/", "In huis"), ("/stijl/", "Stijl"),
                     ("/op-locatie/", "Op locatie"), ("/onderhoud/", "Onderhoud"),
                     ("/journaal/", "Journaal")]),
    ("Deze site", [("/over/", "Over deze site"), ("/contact/", "Contact"),
                   ("/sitemap/", "Sitemap"), ("/privacybeleid/", "Privacybeleid"),
                   ("/cookiebeleid/", "Cookiebeleid")]),
]


def _kruimel(pad):
    if not pad:
        return ""
    delen = ['<a href="/">Home</a>']
    for url, naam in pad[:-1]:
        delen.append('<a href="%s">%s</a>' % (url, html.escape(naam)))
    delen.append("<b>%s</b>" % html.escape(pad[-1][1]))
    return ('<div class="wrap"><div class="kruimel">%s</div></div>'
            % "<span>/</span>".join(delen))


def _jsonld(p, kruimel):
    blokken = []
    if kruimel:
        lijst = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASIS + "/"}]
        for n, (url, naam) in enumerate(kruimel, start=2):
            lijst.append({"@type": "ListItem", "position": n, "name": naam,
                          "item": BASIS + url})
        blokken.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
                        "itemListElement": lijst})
    if p.get("datum"):
        blokken.append({"@context": "https://schema.org", "@type": "Article",
                        "headline": p["titel"], "datePublished": p["datum"],
                        "inLanguage": "nl-NL", "mainEntityOfPage": BASIS + p["url"],
                        "publisher": {"@type": "Organization", "name": NAAM}})
    return "".join('<script type="application/ld+json">%s</script>'
                   % json.dumps(b, ensure_ascii=False) for b in blokken)


def pagina(p, inhoud):
    actief = ""
    for url, _ in MENU:
        if p["url"] == url or (p["url"].startswith(url) and url != "/"):
            actief = url
    nav = "".join('<a href="%s"%s>%s</a>'
                  % (u, ' aria-current="page"' if u == actief else "", html.escape(n))
                  for u, n in MENU)
    voet = "".join('<div class="kolom"><p class="label">%s</p><ul>%s</ul></div>'
                   % (kop, "".join('<li><a href="%s">%s</a></li>' % (u, html.escape(n))
                                   for u, n in links))
                   for kop, links in VOET)
    return """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(titel)s</title>
<meta name="description" content="%(oms)s">
<link rel="canonical" href="%(canoniek)s">
%(robots)s
<meta property="og:type" content="website">
<meta property="og:title" content="%(titel)s">
<meta property="og:description" content="%(oms)s">
<meta property="og:url" content="%(canoniek)s">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#26382e">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="%(naam)s" href="/feed.xml">
<style>%(css)s</style>
%(jsonld)s
</head>
<body>
<div class="top"><div class="wrap">
<a class="naam" href="/">%(merk)s<b>Margriet <i>Bloemdecoraties</i></b></a>
<p class="claim">%(claim)s</p>
</div></div>
<nav class="menubalk" aria-label="Hoofdmenu"><div class="wrap">%(nav)s</div></nav>
%(kruimel)s
<main>%(inhoud)s</main>
<footer>
<div class="wrap">
<div class="kolom">
<p class="label">%(naam)s</p>
<p>Redactionele gids over bloemdecoratie: welke bloemen waar staan, in welke vaas en in
welke verhouding.</p>
<p><a href="mailto:%(mail)s">%(mail)s</a></p>
</div>
%(voet)s
</div>
<div class="voetslot"><div class="wrap"><span>%(naam)s</span>
<span>Redactie in Nederland</span></div></div>
</footer>
</body>
</html>
""" % {
        "titel": html.escape(p["titel"]),
        "oms": html.escape(p["omschrijving"]),
        "canoniek": BASIS + p["url"],
        "robots": '<meta name="robots" content="noindex,follow">' if p.get("noindex") else "",
        "css": theme.CSS,
        "jsonld": _jsonld(p, p.get("kruimel")),
        "merk": theme.MERK_SVG,
        "claim": html.escape(CLAIM),
        "nav": nav,
        "kruimel": _kruimel(p.get("kruimel")),
        "inhoud": inhoud,
        "voet": voet,
        "naam": NAAM,
        "mail": MAIL,
    }
