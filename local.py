# -*- coding: utf-8 -*-
import os
import requests
import base64
import json
import operator

usefulNum=0
uselessNum=0
url = 'http://127.0.0.1:24401/'
path = r"C:\Users\wangggod\Desktop\car_test\deeplearning_data\test_3\new\JPEG"

for filename in os.listdir(path):
    print(filename)
    with open(path+'/'+filename , 'rb') as file:
        img = file.read()
        result = requests.post('http://127.0.0.1:24401/', params={'threshold': 0.1},data=img).json()
        print(result)
        print()
        f = open(r'C:\Users\wangggod\Desktop\car_test\deeplearning_data\test_program\result.txt','a')
        print(result,file=f)
        f.close()
