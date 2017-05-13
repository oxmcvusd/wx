#! /usr/bin/env python'''

#-*-coding:utf-8-*-

import queue
import requests
import json
import datetime
import time
import os
def get_token():

    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {'corpid' : 'wx87780fb826353ecc' ,
              'corpsecret':'qNssAtbS20ZVkjLKP4jf_HF4eHOIBCv0jvce96aYwP1u3rjF7xypoCLvg6vbfCuO',
              }
    req = requests.post(url, params=values)

    j = json.loads(req.text)
    #print (type(j))
    #print (j["access_token"])
    #print (j["expires_in"])
    return j["access_token"]

def send_msg():

    f=open(get_filename(),'r',encoding='gbk')
    #last_line=""
    lines=f.read()#.encode('utf-8')
    
    
    #print (last_line)
    f.close()
    
    
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
    
    dict_arr        = {"touser":"@all",
                       "toparty":"@all",
                       "msgtype":"text",
                       "agentid":"2",
                       "text":
                             {"content":lines},
                       "safe":"0"}

    data   = json.dumps(dict_arr,ensure_ascii=False,indent=2,sort_keys=True).encode('utf-8')
    
    #print (data)
    
    req = requests.post(url,data)
    
    #读取json数据
    j = json.loads(req.text)
    j.keys()
    #print(j)
    if os.path.exists(get_filename()):
        os.remove(get_filename())
    print("均线粘合:"+datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
                  
def get_filename():
    week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    day=datetime.datetime.now().weekday()
    path='C:/'
    fname=path+'交易机会_'+time.strftime('%Y%m%d')+'.txt'
    #print (fname)
    return fname

def loopFun(sched_Timer):
    flag=0
    while True:
        
        now=datetime.datetime.now()
        #print (now)
        if now.strftime('%Y-%m-%d %H-%M-%S')==sched_Timer.strftime('%Y-%m-%d %H-%M-%S'):
        #flag==0:
            
            send_msg()
            flag=1
        else:
            if flag==1:
                sched_Timer=sched_Timer+datetime.timedelta(hours=12) # minutes=1
                flag=0
        #time.sleep(3)
     
def loomf():
    m_flag=time.time()
    while True:
        if os.path.exists(get_filename()):
            statinfo=os.stat(get_filename())
            if m_flag != statinfo.st_mtime:
                send_msg()
                m_flag=statinfo.st_mtime
        time.sleep(60)
if __name__ == '__main__':    
    loomf()
