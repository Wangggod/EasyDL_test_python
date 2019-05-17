# -*- coding: utf-8 -*-
import os
import requests
import base64
import json
import operator

usefulNum=0
uselessNum=0
AccessToken = '24.a635e7b3fd6b5c382df77c079539aece.2592000.1560497779.282335-16249190'
url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/model_1' + '?access_token='+ AccessToken
headers = {'Content-Type' :'application/json'}
path = r"C:\Users\wangggod\Desktop\car_test\deeplearning_data\test_9"

for filename in os.listdir(path):
    print(filename)
    with open(path+'/'+filename , 'rb') as file:
        pic = base64.b64encode(file.read()).decode()
    data = {
        'image':pic,
        "top_num":2
    }
    request = requests.post(url,headers= headers, data=json.dumps(data))
    s=json.loads(request.content)
    #s1=list(json.loads(request.content).items())
    '''
    if operator.eq(s['results'][0]['name'],'useful') ==True:
        usefulNum+1
    else:
        uselessNum+1

    print("useful pic:",usefulNum)
    print("useless pic:",uselessNum)
    '''
    print(s)
    print()
    f = open(r'C:\Users\wangggod\Desktop\car_test\deeplearning_data\test_program\result_9.txt','a')
    print(s,file=f)
    f.close()
