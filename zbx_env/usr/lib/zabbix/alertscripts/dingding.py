#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
import json
import sys
import os
import datetime
webhook = "https://oapi.dingtalk.com/robot/send?access_token=a87ebe756800b76e97b37f1cd964032ebd786fda2873a19ad24228e29eb31bda"
user=sys.argv[1]
subject=sys.argv[2]
text=sys.argv[3]
data={
        "msgtype": "text",
        "text": {
                "content": "%s\r\n%s"%(subject,text)
        },
        "at": {
                "atMobiles": [
                        user
                        ],
                        "isAtAll": False
        }
}
headers = {'Content-Type': 'application/json'}
x=requests.post(url=webhook,data=json.dumps(data),headers=headers)
if os.path.exists("/usr/local/zabbix/log/dingding.log"):
        f=open("/usr/local/zabbix/log/dingding.log","a+")
else:
        f=open("/usr/local/zabbix/log/dingding.log","w+")
f.write("\n"+"--"*30)
if x.json()["errcode"] == 0:
        f.write("\n"+str(datetime.datetime.now())+"    "+str(user)+"    "+"发送成功"+"\n"+str(text))
        f.close()
else:
        f.write("\n"+str(datetime.datetime.now())+"    "+str(user)+"    "+"发送失败"+"\n"+str(text))
        f.close()
