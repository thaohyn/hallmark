"""Bundle index.html, reveal.html and kit.html into self-contained files for Claude Design.

Run from anywhere: python3 standalone/bundle.py. CSS @imports are inlined, and the
reveal.html iframes become srcdoc iframes so each output file needs nothing beside it.
"""
import html, os, re

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, 'standalone')


def css(name):
    text = open(os.path.join(SRC, name)).read()
    return re.sub(r'@import url\("\./([^"]+)"\);', lambda m: css(m.group(1)), text)


def page(name):
    s = open(os.path.join(SRC, name)).read()
    return re.sub(r'<link rel="stylesheet" href="\./([^"]+)">', lambda m: '<style>\n' + css(m.group(1)) + '</style>', s)


reveal = page('reveal.html')


def embed(m):
    query = html.unescape(m.group('q'))
    # srcdoc has no URL query: preset the tier and box in the copy it carries
    doc = reveal.replace("const q = new URLSearchParams(location.search);",
                         "const q = new URLSearchParams(%r);" % query)
    return '<iframe' + m.group('a') + ' srcdoc="' + html.escape(doc, quote=True) + '"' + m.group('b') + '></iframe>'


for name, out in [('index.html', 'qikify-bfcm-landing.html'), ('reveal.html', 'qikify-bfcm-reveal.html'), ('kit.html', 'qikify-bfcm-key-visual.html')]:
    s = page(name)
    s = re.sub(r'<iframe(?P<a>[^>]*?) src="\./reveal\.html\?(?P<q>[^"]*)"(?P<b>[^>]*)></iframe>', embed, s)
    s = s.replace('href="./reveal.html"', 'href="qikify-bfcm-reveal.html"').replace('href="./index.html"', 'href="qikify-bfcm-landing.html"')
    open(os.path.join(OUT, out), 'w').write(s)
    print(out, len(s))
