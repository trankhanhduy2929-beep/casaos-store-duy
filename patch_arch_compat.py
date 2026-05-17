from pathlib import Path
import json

base=Path('Apps')
arch_map = {
    'frigate-nvr': ['amd64','arm64','arm'],
}
for app in sorted(base.iterdir()):
    if not app.is_dir():
        continue
    p=app/'app.json'
    if not p.exists():
        continue
    d=json.loads(p.read_text())
    arch = arch_map.get(app.name, ['amd64','arm64'])
    # broad compatibility aliases
    d['architectures'] = arch
    d['architecture'] = arch
    d['arch'] = arch
    d['supported_architectures'] = arch
    d['unsupported_architectures'] = []
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+"\n")
    print('patched', app.name, arch)

store = Path('AppStore.json')
s = json.loads(store.read_text())
s['architecture'] = ['amd64','arm64']
s['architectures'] = ['amd64','arm64']
s['supported_architectures'] = ['amd64','arm64']
for item in s.get('apps', []):
    arch = ['amd64','arm64','arm'] if item.get('name')=='frigate-nvr' else ['amd64','arm64']
    item['architecture'] = arch
    item['architectures'] = arch
    item['arch'] = arch
    item['supported_architectures'] = arch
store.write_text(json.dumps(s, ensure_ascii=False, indent=2)+"\n")
print('patched AppStore.json')
