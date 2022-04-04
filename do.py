"""import json,os
from re import T
from main import JSON_PATH
def template_error(pid:int)->str:
    返回意外丢失模板
    #temp = '{"code": 0,"data": {"allow_search": false,"attention": 0,"author_title": null,'+\
    #        '"blocked": false,"can_del": false,"comments": [],"cw": null,"likenum": 0,'+\
    #        f'"pid": {pid},'+'"poll": null,"reply": 0,"text": "Not Found","timestamp": 0,"type": "text","url": null}'+'}'
def do(fn):
    pid = int(os.path.split(fn)[-1][:6])
    with open (fn,'rb') as f:
        p = json.load(f)
    if p.get('code')==-1:
        with open (fn,'w+') as f:
            f.write(template_error(pid))
            return pid
for fn in os.listdir(JSON_PATH):
    fn_path = os.path.join(JSON_PATH,fn)
    cod = do(fn_path)
    if cod:
        print(f'{cod} changed')
    else:
        pid = int(os.path.split(fn_path)[-1][:6])
        print(f'{pid} escaped')
to_change_list = [
22319,
22320,
22326,
22327,
22337,
22339,
22350,
22353,
22354,
22358,
22359,
22370,
22402,
22404,
22405,
22417,
22418,
22430,
22440,
22448,
22453,
22455,
22468,
22470,
22479,
22483,
22489,
22490,
22497,
22498,
22502,
22509,
22510,
22516,
22521,
22545,
22558,
22564,
22567,
22588,
22589,
22598,
22610,
22614,
22615,
22616,
22620,
22624,
22625,
22635,
22654,
22666,
22676,
22677,
22678,
22679,
22680,
22699,
22708,
22709,
22710,
22714,
22719,
22749,
22752,
22753,
22757,
22760,
22775,
22776,
22782,
22786,
22817,
22818,
22831,
22832,
22833,
22835,
22836,
22838,
22839,
22842,
22843,
22844,
22855,
22857,
22868,
22869,
22870,
22908,
22909,
22912,
22916,
22920,
22921,
22927,
22933,
22935,
22936,
22956,
22975,
22977,
22979,
22993,
22994,
23019,
23032,
23035,
23059,
23062,
23066,
23089,
23090,
23114,
23116,
23117,
23122,
23146,
23155,
23156,
23173
]
for pid in to_change_list:
    path_name = r'D:\new_hole_crawler_2.0\data\json\%06d.json'%pid
    with open (path_name,'w',encoding='utf-8') as f:
        f.write(template_error(pid))"""

"""import os
img = 'https://bafkreigjpijeaifn2jy7erqpqp6oncse3jmfbo7m7vcdrc4e76evhztyo4.ipfs.dweb.link/?filename=webp.jpg&filetype=image%2Fjpeg'
x = os.path.splitext(img)
print(x)"""
"""import re
IMG_EXTS = ['bmp','jpg','jpeg','png','tif','gif','pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw','WMF','webp','avif','apng']
pattern = '\[.*?\]\((.*?'+'|.*?'.join(IMG_EXTS)+')\)'
t = 'Test\n![](https://bafkreigjpijeaifn2jy7erqpqp6oncse3jmfbo7m7vcdrc4e76evhztyo4.ipfs.dweb.link/?filename=webp.jpg&filetype=image%2Fjpeg)'
print(pattern)
print(re.findall(pattern,t))"""
"""from urllib.request import urlretrieve
url ='https://bot.telegramfiles.ga/23183463851331476/Chairman_Mao.mp4'
urlretrieve(url,'try.mp4')"""