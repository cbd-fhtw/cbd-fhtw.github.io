"""Check rendered local links, assets and HTML fragments; standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1] / '_site'
BASE = '/'

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.links.append(attrs[attr])

docs = {p.resolve(): Document(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
if not docs:
    sys.exit('Keine HTML-Dateien vorhanden. Zuerst quarto render ausführen.')
errors = []
for file, doc in docs.items():
    for link in doc.links:
        u = urlsplit(link)
        if u.scheme or u.netloc:
            continue
        path = unquote(u.path)
        if path.startswith(BASE):
            path = path[len(BASE):]
            target = ROOT / path
        elif path.startswith('/'):
            target = ROOT / path.lstrip('/')
        else:
            target = file.parent / path if path else file
        if target.is_dir():
            target = target / 'index.html'
        target = target.resolve()
        if not target.exists():
            errors.append(f'{file.relative_to(ROOT)}: fehlt {link}')
        elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:
            errors.append(f'{file.relative_to(ROOT)}: Anker fehlt {link}')
if errors:
    sys.exit('\n'.join(errors))
print(f'OK: {len(docs)} HTML-Seiten; interne Links, Assets und Anker geprüft.')
