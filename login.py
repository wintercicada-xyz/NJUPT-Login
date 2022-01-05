#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,socket,sys,getpass,time


try:   #get the username and password
    username,password=sys.argv[1],sys.argv[2]
except IndexError:
    username=input('username:')
    password=getpass.getpass("password:")

post_url='http://p.njupt.edu.cn:801/eportal/'   #url to post login form

params={'c':'ACSetting','a':'Login','protocol':'http:','hostname':'p.njupt.edu.cn','iTermType':'1',
        #'wlanuserip':'', #ip
        'wlanacip':'10.255.253.118','wlanacname':'SPL-BRAS-SR8806-X','mac':'00-00-00-00-00-00',
        #'ip':'',  #ip
        'enAdvert':'0','queryACIP':'0','loginMethod':'1'}  #params for the login url

        # 仙林 wlanacip: 10.255.252.150  wlanacname: XL-BRAS-SR8806-X
        # 三牌楼 wlanacip：10.255.253.118 wlanacname: SPL_BRAS-SR8806-X

data={'DDDDD':',0,'+username+'@cmcc', #',0,'+username+'@cmcc'
      'upass':password,  #password
      'R1':'0','R2':'0','R3':'0','R6':'0','para':'00','0MKKey':'123456','buttonClicked': '','redirect_url': '','err_flag': '','username': '','password': '','user': '','cmd': '','Login': '','v6ip':''} #login form data

def get_ip(): #get host ip
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def login():
    print('login')
    ip=get_ip()
    #params['wlanuserip']=ip
    #params['ip']=ip
    try:
        requests.post(post_url,params=params,data=data)   #login
    except:
        print('login fail')


login() #login