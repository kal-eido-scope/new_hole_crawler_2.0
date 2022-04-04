import argparse

import json
import requests
import os
from tqdm import tqdm
import sys

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data') #data文件夹路径
JSON_PATH = os.path.join(DATA_PATH,'json')                  #json文件夹路径
JSON_PID_LIST = os.listdir(JSON_PATH)                       #json文件夹下pid.json的list
LOG_PATH = os.path.join(DATA_PATH,'log')                    #log文件夹路径
ERROR_JSON_PATH = os.path.join(LOG_PATH,'error_json.json')  #json错误日志路径


API_ROOT = 'https://t-hole.red/_api/v1/'
SPACE = 800
TOKEN = '8wWIP87dNqQaUJIK'
PROXY = {'http':'123.56.231.232'}

def template_error(pid:int,msg:str)->str:
    """返回意外丢失模板"""
    #temp = '{"code": 0,"data": {"allow_search": false,"attention": 0,"author_title": null,'+\
    #        '"blocked": false,"can_del": false,"comments": [],"cw": null,"likenum": 0,'+\
    #        f'"pid": {pid},'+'"poll": null,"reply": 0,"text": "Not Found","timestamp": 0,"type": "text","url": null}'+'}'
    temp = """{"code": -1,"data": {"allow_search": true,"attention": false,"author_title": null,"blocked": false,"blocked_count": null,"can_del": false,"""+\
        """"comments": null,"create_time": "1970-01-01T08:00:00.000000Z","cw": null,"hot_score": null,"is_blocked": false,"is_reported": null,"is_tmp": false,"""+\
        """"last_comment_time": "1970-01-01T08:00:00.000000Z","likenum": 0,"n_attentions": 0,"n_comments": 0,"pid": %d,"poll": null,"reply": 0,"text": "%s","timestamp": 0}}"""%(pid,msg)
    return temp

def write_error(pid:int,status_code:int,data_json:dict)->bool:
    """写入错误代码，返回是否已存在，避免删除后覆盖"""
    error_code = data_json.get(pid)
    exist = True if error_code else False
    data_json[pid]=status_code
    return exist
    
def get_content(pid:int,s:requests.Session,data_json:dict)->int:
    GET_URL = API_ROOT + '/getone?pid=' + str(pid)
    post_path = os.path.join(DATA_PATH, 'json','%06d.json'%pid)
    headers = {'User-Token': TOKEN}
    r = s.get(GET_URL,headers=headers)
    if r.status_code != 200:
        if r.status_code == 429:
            sys.exit('Too many requests!')
        exist_flag = write_error(pid,r.status_code,data_json)
        if not exist_flag:
            if f'{pid}.json' not in JSON_PID_LIST:
                with open (post_path,'w',encoding='utf-8') as f:
                    f.write(template_error(pid,'Unknown error'))
        return r.status_code
    else:
        if r.json()['code']==-1:
            with open (post_path,'w',encoding='utf-8') as f:
                f.write(template_error(pid,r.json()['msg']))
            return 200
        else:
            req = r.json()
            os.makedirs(os.path.dirname(post_path), exist_ok=True)
            with open(post_path,'wb+') as f:
                f.write(json.dumps(req,ensure_ascii=False).encode('utf8'))
            return r.status_code

def get_cur_pid()->int:
    json_list = []
    for file_name in os.listdir(JSON_PATH):
        json_list.append(int(os.path.splitext(file_name)[0]))
    if json_list:
        json_list.sort()
        return json_list[-1]
    else:
        return SPACE+1

def get_max_pid(s:requests.Session)->int:
    """获取最新id"""
    GET_PAGE = API_ROOT + '/getlist?p=1&order_mode=0'
    headers = {'User-Token': TOKEN}
    r = s.get(GET_PAGE,headers=headers)
    max_pid = r.json()['data'][0]['pid']
    if type(max_pid)==int:
        return max_pid
    else:
        return 19000    #暂定意外19000

def process_start_end(start:int,end:int,mp:int)->tuple:
    """返回开始项和结束项"""
    if start:
        if start >= mp:
            return mp-SPACE,mp
        if end:
            if end >= mp:
                return start,mp
            else:
                if end <= start:
                    start,end = end,start
                return start,end
        else:
            return start,min(mp,start+SPACE)
    else:
        cur_pid = get_cur_pid()    
        return cur_pid,min(cur_pid+SPACE,mp)

def scan_mode(mp:int)->tuple:
    """开启扫描模式"""
    SCAN_PID = os.path.join(LOG_PATH,'scan_pid.txt')
    with open(SCAN_PID,'w+')as f:
        last_scan = int(f.read())
        if last_scan+SPACE >= mp:
            f.write(1)
        else:
            f.write(last_scan+SPACE)
    return process_start_end(last_scan,last_scan+SPACE,mp)

def main():
    parser = argparse.ArgumentParser('New T-Hole Crawler')
    parser.add_argument('--token',type=str,help='token')#, required=True
    parser.add_argument('--start', type=int, help='Inclusion')#, required=True
    parser.add_argument('--end', type=int , help='Exclusion') #, required=True
    parser.add_argument('--scan', type=bool , help='Scan Mode') #, required=True
    args = parser.parse_args()
    s = requests.Session()
    max_pid = get_max_pid(s)    #获取最新id
    try:
        with open (ERROR_JSON_PATH,'r') as f:
            data_json = json.load(f)    #载入错误列表
    except:
        data_json = {}
    f = open (ERROR_JSON_PATH,'w+')     #打开错误列表写入状态
    try:
        start_id,end_id = scan_mode(max_pid) if args.scan else process_start_end(args.start,args.end,max_pid)
        #start_id,end_id = 23268,23269
        for pid in tqdm(range(start_id,end_id), desc='Posts'):
            st_code = get_content(pid,s,data_json)
            tqdm.write(f'Request post:{pid},status_code:{st_code}')
        json.dump(data_json,f)
    except:
        json.dump(data_json,f)          #意外错误恢复错误列表
    f.close()

if __name__ == '__main__':
    main()