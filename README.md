# new_hole_crawler_2.0

## 需要安装的包
```
pip install tqdm,argparse,requests
```
or
```
pip3 install tqdm,argparse,requests
```

## 使用说明

### main.py 爬虫
```
python main.py    --token xxxxxx          此项目暂未生效
                  --start xxxxxx          开始项，若未指定则扫描已有json数据库，并从pid最大项开始
                  --end   xxxxxx          结束项，若未指定则从开始项向后扫描500条，直至最新pid
                  --scan  true/false      扫描模式，默认关闭，若开启，则从pid=1开始进行扫描，并记录扫描位置
```
### img_down.py 下载图片
```
python img_down.py --start xxxxxx         开始项，若未指定则扫描已有img数据库，并从pid最大项开始
                   --scan  true/false     扫描模式，同上
                   --end   xxxxxx         结束项，若未指定读取当前json数据最大值
                                          若结束项小于开始项，则跳出
```

### img_confirm.py 确认图片
```
python img_confirm.py
```
利用imghdr确认图片是否可打开（常用图片格式），imghdr对jpg和jpeg文件识别不佳
### img_reload.py 重新加载图片
```
python img_reload.py  --d bool            未下载部分重新下载
                      --e bool            非图片（已损坏部分）重新下载
```
为防止意外未能下载的图片，重新加载

### mov_down.py 下载视频
```
python mov_down.py    --start xxxxxx      开始项，若未指定则扫描已有mov数据库，并从pid最大项开始
                      --scan  true/false  扫描模式，同上
                      --end   xxxxxx      结束项，若未指定读取当前json数据最大值
                                          若结束项小于开始项，则跳出
```
### mov_reload.py 重新加载视频
```
python mov_reload.py  --d bool            未下载部分重新下载
```
为防止意外未能下载的视频，重新加载
**注：以上pid,img,mov目前均设置为最新SPACE条循环扫描**

### 特点
* 包含日志文件，见[data/log](https://github.com/kal-eido-scope/new_hole_crawler_2.0/tree/main/data/log)部分

### 参数设置
```
SPACE   基础间隔，用于指定默认单次爬虫条目，默认500
TOKEN   自定义token
```

## 待实现功能
* 确定不同扫描模式，如定期从头开始，最新条目等

