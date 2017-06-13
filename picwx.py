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

def get_pic():
    from PIL import ImageGrab
    #im=ImageGrab.grab()
    pic='C:/222'+".jpg"
    #im.save(pic)
    
    #img_url='https://api.weixin.qq.com/cgi-bin/material/add_material'
    img_url='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
    payload={
        'access_token':get_token(),
        'type':'image'#,
        #'media':open(pic,'rb')
        }
    print(payload)
    data={'media':pic}#open(pic,'rb')
    print(data)
    #r=requests.post(url=img_url,params=payload,files=data)#
    r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+get_token()+'&type=image',files=data)
    print(r)
    if r.status_code==200:
        dicts =r.json()
        print (dicts)
        print (dicts['media_id'])
        return dicts['media_id']
    
def send_pic():

                        url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
                        data        = {"touser":"@all",
                                           "toparty":"@all",
                                           "msgtype":"image",
                                           "agentid":"3",
                                           "image":{"media_id":get_pic()},
                                           "safe":"0"}
                        #data   = json.dumps(dict_arr,ensure_ascii=False,indent=2,sort_keys=True).encode('utf-8')
                        req = requests.post(url,data=json.dumps(data))
                        #读取json数据
                        j = json.loads(req.text)
                        j.keys()
                        #print (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
                        print(j)
if __name__ == '__main__':
            while True:
                        send_pic()
                        time.sleep(35)
                 
