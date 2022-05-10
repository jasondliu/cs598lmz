import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

import sys
print(sys.executable)

import os
print(os.getcwd())

import re
print(re.search(r'\d+', '33b'))

import json
print(json.load(open('info.json')))

import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d'))

import time
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

import smtplib
from email.mime.text import MIMEText
msg = MIMEText('hello world', 'plain', 'utf-8')
# send email
try:
    server = smtplib.SMTP_SSL('smtp.163.com', 465)
    server.login('xxx@163.com', 'xxx')
    server.sendmail('xxx@163.com', 'xxx@qq.com', msg.as_string())
    server.quit
