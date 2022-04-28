import os
import json
import re
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
JSON_PATH = os.path.join(DATA_PATH,'json')
RESULT_PATH = os.path.join(os.path.dirname(__file__),'result.json')
def find(text:str)->dict:
    result = {}
    result['text']=text
    result['data']={}
    for fn in os.listdir(JSON_PATH):
        pid = int(os.path.splitext(fn)[0])
        temp_result = []
        f = os.path.join(JSON_PATH,fn)
        with open(f,'r',encoding='utf-8')as fp:
            p = json.load(fp)
        to_find = [p['data']['text']]
        if p['data']['comments']:
            for comment in p['data']['comments']:
                to_find.append(comment['text'])
        for txt in to_find:
            matches  = re.findall(text,txt)
            if matches:
                temp_result.append(txt)
        if temp_result:
            result['data'][pid] = temp_result
        print('%d finished'%pid)
    return result

def main():
    text = input('Enter what you want to find:\n')
    result = find(text)
    with open(RESULT_PATH,'ab+')as f:
        f.write(json.dumps(result,ensure_ascii=False,indent=4).encode('utf-8'))
    print(json.dumps(result,ensure_ascii=False,indent=4))
if __name__ == '__main__':
    main()