# -*- coding: utf-8 -*-
import os
import requests
import base64
import json

AccessToken = '24.a635e7b3fd6b5c382df77c079539aece.2592000.1560497779.282335-16249190'
url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/model_1' + '?access_token='+ AccessToken
headers = {'Content-Type' :'application/json'}

for filename in os.listdir(r"./"):
    print(filename)
    with open(filename , 'rb') as file:
        pic = base64.b64encode(file.read()).decode()
    data = {
        'image':pic,
        "top_num":5
    }
    request = requests.post(url,headers= headers, data=json.dumps(data))
    print(json.loads(request.content))
    