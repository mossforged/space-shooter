"""Rebuild the self-contained offline game and update the deployed HTML hash."""
from pathlib import Path
import base64
import hashlib
import json
import mimetypes
import re
import zipfile

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
release = json.loads((root / 'release.json').read_text())
archive = root / release['download']
with zipfile.ZipFile(archive) as old:
    supporting = {i.filename: old.read(i) for i in old.infolist() if not i.filename.endswith('.html')}

def embed(match):
    path = root / match[1]
    mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return '"data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode() + '"'

offline = re.sub(r'"(assets/[^"\n]+)"', embed, html)
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as out:
    out.writestr('Void_Crew_Prototype_0_18.html', offline)
    for name, data in supporting.items():
        out.writestr(name, data)
release['html_sha256'] = hashlib.sha256(html.encode()).hexdigest()
release['revision'] = 'traversal-1'
(root / 'release.json').write_text(json.dumps(release, indent=2) + '\n')
print('Rebuilt offline ZIP; HTML SHA-256:', release['html_sha256'])
