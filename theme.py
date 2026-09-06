# -*- coding: utf-8 -*-
"""Vormgeving en sjabloon van margrietbloemdecoraties.nl."""

CSS = """
:root{
  --ivoor:#f5f2ea; --wit:#fbfaf6; --inkt:#171612; --zacht:#57544a;
  --lijn:#ddd6c6; --lijn-fijn:#e9e3d6; --groen:#26382e; --oker:#9b7729; --klei:#b9a88a;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ivoor);color:var(--inkt);
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  font-size:18px;line-height:1.7}
img{max-width:100%;height:auto}
a{color:var(--groen);text-underline-offset:3px}
a:hover{color:var(--oker)}
.wrap{width:min(1140px,calc(100% - 44px));margin-inline:auto}
.label{font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;font-size:11.5px;
  letter-spacing:.22em;text-transform:uppercase;color:var(--zacht);font-weight:600}

/* kopbalk in twee lagen */
.top{border-bottom:1px solid var(--lijn)}
.top .wrap{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;
  padding:26px 0 16px;flex-wrap:wrap}
.naam{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--inkt)}
.naam b{font-weight:400;font-size:27px;letter-spacing:.01em;line-height:1}
.naam b i{font-style:italic;color:var(--oker)}
.claim{font-size:13px;color:var(--zacht);max-width:34ch;text-align:right;line-height:1.45}
.menubalk{border-bottom:1px solid var(--lijn);background:var(--wit);position:sticky;top:0;z-index:9}
.menubalk .wrap{display:flex;gap:26px;flex-wrap:wrap;padding:0}
.menubalk a{font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;font-size:13px;
  letter-spacing:.13em;text-transform:uppercase;text-decoration:none;color:var(--zacht);
  padding:14px 0;border-bottom:2px solid transparent;font-weight:600}
.menubalk a:hover{color:var(--inkt)}
.menubalk a[aria-current]{color:var(--inkt);border-bottom-color:var(--oker)}

.kruimel{font-size:13px;color:var(--zacht);padding:20px 0 0;
  font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif}
.kruimel a{color:var(--zacht);text-decoration:none}
.kruimel a:hover{color:var(--oker)}
.kruimel span{padding:0 8px;opacity:.5}

h1{font-size:clamp(32px,4.6vw,50px);line-height:1.08;font-weight:400;margin:.35em 0 .35em;
  letter-spacing:-.01em}
h2{font-size:clamp(22px,2.5vw,28px);font-weight:400;line-height:1.25;margin:1.9em 0 .5em}
h3{font-size:20px;font-weight:600;margin:1.5em 0 .35em}
p{margin:0 0 1.1em}
.lood{font-size:21px;line-height:1.55;color:#33302a;max-width:46ch}
ul,ol{margin:0 0 1.2em;padding-left:1.2em}
li{margin:.35em 0}
li::marker{color:var(--oker)}

/* opening van de home */
.opening{border-bottom:1px solid var(--lijn)}
.opening .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;
  padding:56px 0 46px;align-items:center}
.opening h1{max-width:20ch}
.vaasvlak{width:100%;max-width:360px;margin-left:auto;display:block}
.streep{width:56px;height:1px;background:var(--oker);margin:22px 0}

/* genummerde rijen */
.index{list-style:none;padding:0;margin:8px 0 0;border-top:1px solid var(--lijn)}
.index li{border-bottom:1px solid var(--lijn-fijn)}
.index a{display:grid;grid-template-columns:60px 1fr auto;gap:22px;align-items:baseline;
  padding:17px 0;text-decoration:none;color:inherit}
.index a:hover{background:rgba(155,119,41,.05)}
.index .nr{font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;font-size:12px;
  letter-spacing:.14em;color:var(--oker);font-weight:700}
.index .titel{font-size:20px}
.index .toe{font-size:14.5px;color:var(--zacht);max-width:46ch;
  font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif}
@media(max-width:720px){
  .index a{grid-template-columns:38px 1fr;gap:12px}
  .index .toe{grid-column:2;max-width:none}
}

/* tekstpagina met meelopende index */
.kolommen{display:grid;grid-template-columns:210px 1fr;gap:52px;
  align-items:start;padding-top:8px}
.zij{position:sticky;top:78px;padding-top:8px}
.zij ol{list-style:none;padding:0;margin:10px 0 0;border-left:1px solid var(--lijn)}
.zij li{margin:0}
.zij a{display:block;padding:6px 0 6px 14px;font-size:14px;text-decoration:none;
  color:var(--zacht);border-left:2px solid transparent;margin-left:-1px;line-height:1.35}
.zij a:hover{color:var(--inkt);border-left-color:var(--oker)}
article{max-width:70ch}
@media(max-width:900px){.kolommen{grid-template-columns:1fr;gap:0}.zij{display:none}}

/* blokken */
.uitgelicht{border-top:1px solid var(--oker);border-bottom:1px solid var(--oker);
  padding:16px 0;margin:1.8em 0;font-size:19px;font-style:italic;color:#2c2a24}
.uitgelicht p{margin:0}
.winkel{border:1px solid var(--lijn);background:var(--wit);padding:22px 26px;margin:2.4em 0 1em}
.winkel h2{margin:0 0 8px;font-size:21px}
.winkel p:last-child{margin-bottom:0}
.tabelwrap{overflow-x:auto;margin:1.5em 0}
table{border-collapse:collapse;width:100%;min-width:440px;font-size:16px;
  font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif}
th,td{text-align:left;padding:11px 14px 11px 0;border-bottom:1px solid var(--lijn-fijn);
  vertical-align:top}
th{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--zacht);
  border-bottom:1px solid var(--lijn)}

.band{background:var(--groen);color:#eae5d8;margin-top:58px}
.band .wrap{padding:46px 0}
.band h2{margin-top:0;color:#fff}
.band .label{color:#b9c7ba}
.band a{color:#f0e9d8}
.principes{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin-top:8px}
.principes h3{margin:.2em 0 .3em;font-weight:400;font-size:21px;color:#fff}
.principes p{font-size:15.5px;color:#cfd8cd;margin:0}
.principes .nr{font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;
  font-size:11.5px;letter-spacing:.2em;color:#a9bcab;font-weight:700}
@media(max-width:820px){.principes{grid-template-columns:1fr;gap:22px}}

.journaal{list-style:none;padding:0;margin:0;border-top:1px solid var(--lijn)}
.journaal li{border-bottom:1px solid var(--lijn-fijn)}
.journaal a{display:grid;grid-template-columns:110px 1fr;gap:22px;padding:16px 0;
  text-decoration:none;color:inherit;align-items:baseline}
.journaal a:hover{color:var(--oker)}
.journaal .dat{font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;font-size:12.5px;
  letter-spacing:.1em;color:var(--zacht)}
.journaal .kop{font-size:19.5px}
@media(max-width:620px){.journaal a{grid-template-columns:1fr;gap:4px}}

main{padding-bottom:20px}
section.blok{padding:46px 0 8px}
section.blok.lijn{border-top:1px solid var(--lijn)}

footer{border-top:1px solid var(--lijn);margin-top:64px;background:var(--wit)}
footer .wrap{padding:34px 0 12px;display:flex;gap:34px;flex-wrap:wrap;
  justify-content:space-between;align-items:flex-start}
footer .kolom{max-width:34ch}
footer p{font-size:15px;color:var(--zacht)}
footer ul{list-style:none;padding:0;margin:8px 0 0;
  font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif;font-size:14.5px}
footer li{margin:.3em 0}
footer a{color:var(--inkt);text-decoration:none}
footer a:hover{color:var(--oker);text-decoration:underline}
.voetslot{border-top:1px solid var(--lijn-fijn);font-size:13px;color:var(--zacht);
  font-family:ui-sans-serif,"Segoe UI",Helvetica,Arial,sans-serif}
.voetslot .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;
  padding:14px 0 26px}

@media(max-width:860px){
  .opening .wrap{grid-template-columns:1fr;gap:30px;padding:38px 0 34px}
  .vaasvlak{max-width:230px;margin:0}
  .claim{text-align:left}
}
@media(max-width:560px){body{font-size:17px}
  .menubalk .wrap{gap:15px}
  .menubalk a{font-size:11.5px;letter-spacing:.1em;padding:11px 0}
  .claim{display:none}
  .naam b{font-size:23px}}
"""


def _pluim(x, y, hoek, lengte, kleur, dicht=13):
    """Een grasachtige pluim: een steel met fijne zijharen."""
    haren = []
    for n in range(dicht):
        t = n / float(dicht - 1)
        hy = -lengte * (0.30 + 0.70 * t)
        breedte = 15 * (1 - abs(t - 0.45) * 1.5)
        if breedte < 3:
            breedte = 3
        for kant in (-1, 1):
            haren.append(
                '<path d="M0 %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" stroke="%s" '
                'stroke-width="1.5" fill="none" stroke-linecap="round" opacity=".85"/>'
                % (hy, kant * breedte * .35, hy - 3, kant * breedte * .75, hy - 7,
                   kant * breedte, hy - 12, kleur))
    return ('<g transform="translate(%s %s) rotate(%s)">'
            '<path d="M0 0 C1 %.1f -1 %.1f 0 %.1f" stroke="%s" stroke-width="2.2" '
            'fill="none" stroke-linecap="round"/>%s</g>'
            % (x, y, hoek, -lengte * .4, -lengte * .7, -lengte, kleur, "".join(haren)))


def _bol(x, y, hoek, lengte, kleur, bolkleur, straal=11):
    return ('<g transform="translate(%s %s) rotate(%s)">'
            '<path d="M0 0 C2 %.1f -2 %.1f 0 %.1f" stroke="%s" stroke-width="2.2" '
            'fill="none" stroke-linecap="round"/>'
            '<circle cy="%.1f" r="%s" fill="%s"/>'
            '<circle cy="%.1f" r="%s" fill="#fff" opacity=".18"/></g>'
            % (x, y, hoek, -lengte * .4, -lengte * .7, -lengte, kleur,
               -lengte - straal * .5, straal, bolkleur, -lengte - straal * .9, straal * .45))


def _bloesemtak(x, y, hoek, kleur, bloemkleur, hart):
    bloemen = []
    for hoogte, schaal, zij in ((-52, .58, -13), (-88, .74, 9), (-124, .62, -8),
                                (-150, .48, 12)):
        blad = "".join(
            '<ellipse rx="9" ry="4.6" transform="rotate(%d) translate(9 0)" fill="%s"/>'
            % (h, bloemkleur) for h in (0, 60, 120, 180, 240, 300))
        bloemen.append('<g transform="translate(%d %d) scale(%.2f)">%s'
                       '<circle r="4.2" fill="%s"/></g>' % (zij, hoogte, schaal, blad, hart))
    return ('<g transform="translate(%s %s) rotate(%s)">'
            '<path d="M0 0 C6 -50 -6 -104 2 -158" stroke="%s" stroke-width="3" fill="none" '
            'stroke-linecap="round"/>'
            '<path d="M2 -70 C16 -84 26 -92 34 -96" stroke="%s" stroke-width="2.2" '
            'fill="none" stroke-linecap="round"/>%s</g>'
            % (x, y, hoek, kleur, kleur, "".join(bloemen)))


def _blad(x, y, hoek, schaal, kleur):
    return ('<g transform="translate(%s %s) rotate(%s) scale(%s)">'
            '<path d="M0 0 C18 -10 34 -8 44 2 C32 12 14 12 0 0 Z" fill="%s"/>'
            '<path d="M2 1 C16 2 30 3 42 2" stroke="#fff" stroke-opacity=".35" '
            'stroke-width="1.4" fill="none"/></g>' % (x, y, hoek, schaal, kleur))


HELD_SVG = """
<svg class="vaasvlak" viewBox="0 0 360 380" role="img"
     aria-label="Illustratie van een bloemdecoratie met takken, pluimen en zaaddozen">
  <defs>
    <linearGradient id="keramiek" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#f0e8d8"/><stop offset=".38" stop-color="#e3d7bf"/>
      <stop offset="1" stop-color="#bfab8b"/>
    </linearGradient>
  </defs>
  <line x1="24" y1="332" x2="336" y2="332" stroke="#ded7c7"/>
  %(takken)s
  <path d="M138 224 c-8 12 -12 27 -12 44 c0 30 6 52 12 62 h84 c6 -10 12 -32 12 -62
           c0 -17 -4 -32 -12 -44 z" fill="url(#keramiek)"/>
  <ellipse cx="180" cy="224" rx="42" ry="7" fill="#c7b393"/>
  <ellipse cx="180" cy="224" rx="33" ry="4.6" fill="#a8977a"/>
  <path d="M152 240 c-6 24 -6 60 -1 88" stroke="#fff" stroke-opacity=".5" stroke-width="5"
        fill="none" stroke-linecap="round"/>
  <ellipse cx="180" cy="332" rx="52" ry="7" fill="#e8e1d1"/>
</svg>
""" % {"takken": "".join([
    _pluim(150, 226, -16, 150, "#8a9179"),
    _pluim(168, 226, -5, 176, "#7c8a6d"),
    _pluim(206, 226, 13, 158, "#8a9179"),
    _bloesemtak(186, 228, 8, "#5c6f57", "#f3ece0", "#c9a227"),
    _bloesemtak(160, 228, -14, "#6b7d62", "#e8dac6", "#b98a3c"),
    _bol(196, 226, 24, 96, "#7c8a6d", "#c9a227"),
    _bol(148, 226, -28, 82, "#7c8a6d", "#b9a88a"),
    _bol(178, 226, 2, 120, "#6b7d62", "#9b7729"),
    _blad(150, 206, 196, 0.9, "#6f8163"),
    _blad(212, 212, -20, 0.8, "#7e8f70"),
])}

MERK_SVG = ('<svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true">'
            '<circle cx="16" cy="16" r="15" fill="none" stroke="#9b7729"/>'
            '<g fill="#26382e">'
            '<path d="M16 7c2 3 2 6 0 9-2-3-2-6 0-9z"/>'
            '<path d="M16 25c-2-3-2-6 0-9 2 3 2 6 0 9z"/>'
            '<path d="M7 16c3-2 6-2 9 0-3 2-6 2-9 0z"/>'
            '<path d="M25 16c-3 2-6 2-9 0 3-2 6-2 9 0z"/></g>'
            '<circle cx="16" cy="16" r="2.2" fill="#9b7729"/></svg>')

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="4" fill="#f5f2ea"/>'
           '<g fill="#26382e">'
           '<path d="M16 6c2.2 3.4 2.2 6.6 0 10-2.2-3.4-2.2-6.6 0-10z"/>'
           '<path d="M16 26c-2.2-3.4-2.2-6.6 0-10 2.2 3.4 2.2 6.6 0 10z"/>'
           '<path d="M6 16c3.4-2.2 6.6-2.2 10 0-3.4 2.2-6.6 2.2-10 0z"/>'
           '<path d="M26 16c-3.4 2.2-6.6 2.2-10 0 3.4-2.2 6.6-2.2 10 0z"/></g>'
           '<circle cx="16" cy="16" r="2.4" fill="#9b7729"/></svg>\n')
