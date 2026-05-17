from pathlib import Path
import json
base=Path('Apps')
port_map={
    '9router':'20128','frigate-nvr':'5000','github-release-guard':'5566','personal-timesheet':'5555',
    'picoclaw-ai':'18800','shop-admin':'1235','web-thi-ai-bao-mat':'1234','yduc-booking-v2':'3008'
}
category_map={
    '9router':'Network','frigate-nvr':'Surveillance','github-release-guard':'Developer','personal-timesheet':'Productivity',
    'picoclaw-ai':'AI','shop-admin':'Business','web-thi-ai-bao-mat':'Education','yduc-booking-v2':'Business'
}
for app in sorted(base.iterdir()):
    if not app.is_dir():
        continue
    p=app/'app.json'
    if not p.exists():
        continue
    data=json.loads(p.read_text())
    data['architectures']=['amd64','arm64','arm'] if app.name=='frigate-nvr' else ['amd64','arm64']
    data['version']='1.0.1'
    data['category']=category_map.get(app.name,'Utilities')
    data['port_map']=port_map.get(app.name,'')
    data['store_app_id']=app.name if app.name!='frigate-nvr' else 'frigate-nvr-duy'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
    print('patched', app.name)
