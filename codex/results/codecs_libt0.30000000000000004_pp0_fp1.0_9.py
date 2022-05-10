import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 导入需要的库
import sys
import os
import json
import time
import requests
from bs4 import BeautifulSoup

# 全局变量
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

# 创建文件夹
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 获取网页信息
def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:

