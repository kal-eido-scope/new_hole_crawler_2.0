"""import requests"""
"""headers ={
			"Accept": "*/*",
			"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
			"Connection":"keep-alive",
			"Host": "t-hole.red",
			"Referer": "https://t-hole.red/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
			"TE": "trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
			"User-Token": "8wWIP87dNqQaUJIK"
			}
pid = 21466
GET_URL = 'https://t-hole.red/_api/v1/'+ '/getone?pid=' + str(pid)
r = requests.get(GET_URL,headers=headers)
print(r.json())"""
"""l = []
with open('s.js','w+')as f:
    for x in range(1,1001):
        l.append("")"""
import os,json
from main import JSON_PATH
logf = open('log.txt','w+')
for fn in os.listdir(JSON_PATH):
	pid = int(os.path.splitext(fn)[0])
	f = os.path.join(JSON_PATH,fn)
	#f = r'D:\new_hole_crawler_2.0\data\json\000004.json'
	with open(f,'r',encoding='utf-8')as fp:
		p = json.load(fp)

	new_comments = []
	if p['data']['comments']:
		for temp in p['data']['comments']:
			if temp.get('pid'):	#旧的
				flag = True
				for comp in p['data']['comments']:
					if temp['timestamp'] == comp['timestamp']:
						if temp['name_id'] == comp['name_id']:
							if temp['text'] == comp['text']:
								if comp.get('pid') is None:
									flag = False
				if flag:
					new_version = {
					"author_title": temp['author_title'],
					"blocked": temp['blocked'],
					"blocked_count": 0,
					"can_del": temp['can_del'],
					"cid": -1,
					"create_time": temp['timestamp'],
					"is_blocked": False,
					"is_tmp": False,
					"name_id": temp['name_id'],
					"text": temp['text'],
					"timestamp": temp['timestamp']
					}
					new_comments.append(new_version)
					logf.write('%d  one old comment has been modified and added\n'%pid)
					print('%d  one old comment has been modified and added')
				else:
					logf.write('%d one old comment has been removed.\n'%pid)
					print('%d  one old comment has been removed')
			else:
				new_comments.append(temp)
				logf.write('%d one new comment has been keeped.\n'%pid)
		final_comments = sorted(new_comments,key = lambda x:x['cid'])
	p['data']['comments'] = final_comments
	with open(f,'wb+')as fw:
		fw.write(json.dumps(p,ensure_ascii=False).encode('utf-8'))
		print('%d written'%pid)
	#break
logf.close()