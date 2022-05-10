import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import random
import requests
import datetime
import traceback
import threading
from bs4 import BeautifulSoup

from config import *
from db import *

def get_crawl_list(start_page = 1, end_page = -1):
    '''
    获取待爬取的网页列表
    '''
    # 初始化数据库
    db = DB()
    # 获取爬取网页列表
    crawl_list = db.get_crawl_list(start_page, end_page)
    # 关闭数据库
    db.close()
    return crawl_list

def get_proxy():
    '''
    获取代理ip
    '
