import os,argparse,json,sys
from mov_down import MOV_PATH,ERROR_MOV_PATH,format_mov_name,get_type, url_down
from urllib.request import urlretrieve
def reload_movie(error_mov_log:dict):
    for pid_str,values in error_mov_log.copy().items():
        pid = int(pid_str)
        os.makedirs(os.path.join(MOV_PATH,'%0d'%pid), exist_ok=True)
        urls = [list(x.keys()) for x in values]
        url_dict = get_type(urls)
        flag = True
        for url,ext in url_dict.items():
            url_name = format_mov_name(url,ext)
            mov_path = os.path.join(MOV_PATH,'%0d'%pid,url_name)
            try:
                url_down(url,mov_path)
            except:
                print('%d\tA movie failed.'%pid)
                flag = False
        if flag:
            error_mov_log.pop(pid_str)
            print('%d\tAll movie(s) downloaded successfully.'%pid)
        else:
            print('%d\tSome movie(s) failed to be downloaded.'%pid)

def main():
    parser = argparse.ArgumentParser('T-hole.red Mov reload')
    parser.add_argument('--d', type=bool, help='Not downloaded')
    #parser.add_argument('--e', type=bool, help='Not a movie')
    args = parser.parse_args()
    if args.d is None :#and args.e is None
        print('Nothing Activated')
    if args.d:
        try:
            with open(ERROR_MOV_PATH,'r')as f:
                error_mov_log = json.load(f)
            reload_movie(error_mov_log)
        except:
            sys.exit()
        try:
            with open(ERROR_MOV_PATH,'w+')as f:
                json.dump(error_mov_log,f)
        except:
            pass

if __name__ == '__main__':
    main()