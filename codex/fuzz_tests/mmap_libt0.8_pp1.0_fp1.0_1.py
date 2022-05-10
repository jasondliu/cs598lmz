import mmap
import random
import time
from datetime import datetime, timedelta

from headers import get_headers
from ip_pool import get_ip_pool
from useragents import get_useragents


# 封装日志方法
def write_log(msg):
    # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('spider.log', 'a+') as f:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg, file=f)
        print(file=f)


# 发送验证码
def send_code(name):
    print("发送验证码")
    url = 'https://qy.58.com/index/index/sendcode'
    form_data = {
        'phone': name
    }
    headers = {
        'Accept': '*/*',
        'Origin
