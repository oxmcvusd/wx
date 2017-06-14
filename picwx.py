#! /usr/bin/env python'''

#-*-coding:utf-8-*-
import queue
import requests
import json
import datetime
import time
import os
import csv


def get_token():
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {'corpid' :'wx87780fb826353ecc',# 'wx87780fb826353ecc' ,#
              'corpsecret':'jrZvrrQ1Q_zICTbZas651lO7p0jhxLdo3kQ0Pz2fAI_9O_H7YDGUB6qmrqE9dX0y'#'jrZvrrQ1Q_zICTbZas651lO7p0jhxLdo3kQ0Pz2fAI_9O_H7YDGUB6qmrqE9dX0y',#04d468d79d4ade68f49c58d4a5bd481f
              }
    req = requests.post(url, params=values)
    j = json.loads(req.text)
    print (j)
    print(j["access_token"])
    return j["access_token"]
def screen_shot():
    from PIL import ImageGrab
    im=ImageGrab.grab()
    pic='C:/Users/Administrator/Documents/tbv5321_x64_portable/'+time.strftime('%Y-%m-%d %H-%M-%S')+".jpg"
    im.save(pic)
    #pic='C:/222'+".jpg"
    return pic

def post_pic():
    #from PIL import ImageGrab
    #im=ImageGrab.grab()
    #pic='C:/222'+".jpg"
    #im.save(pic)
    
    #img_url='https://api.weixin.qq.com/cgi-bin/material/add_material'
    img_url='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
    payload={
        'access_token':get_token(),
        'type':'image'#,
        #'media':open(screen_shot(),'rb')
        }
    print(payload)
    data={'media':open(screen_shot(),'rb')}#
    print(data)
    #r=requests.post(url=img_url,params=payload,files=data)#
    r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+get_token()+'&type=image',files=data)
    print(r)
    if r.status_code==200:
        dicts =r.json()
        print (dicts)
        print (dicts['media_id'])
        return dicts['media_id']
    
def get_pic():

                        #url="https://qyapi.weixin.qq.com/cgi-bin/media/get?access_token="+get_token()+"&media_id="+post_pic()
                        #print(url)
                        url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
                        data        = {"touser":"@all",
                                           "toparty":"@all",
                                           "msgtype":"image",
                                           "agentid":"3",
                                           "image": {
                                               "media_id":post_pic()
                                                },
                                           "safe":"0"}
  
                        #data   = json.dumps(dict_arr,ensure_ascii=False,indent=2,sort_keys=True).encode('utf-8')
                        req = requests.post(url,data=json.dumps(data))
                        #读取json数据
                        j = json.loads(req.text)
                        j.keys()
                        print (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
                        print(j)
def time_control():
    current_time=time.localtime(time.time())
    if((current_time.tm_hour==21 or current_time.tm_hour==9 or current_time.tm_hour==12 or current_time.tm_hour==15) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
        get_pic()
        
if __name__ == '__main__':
            while True:
                    time_control()
                    time.sleep(1)
                 
