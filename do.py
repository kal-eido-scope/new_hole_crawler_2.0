import requests
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
l = []
with open('s.js','w+')as f:
    for x in range(1,1001):
        l.append("")