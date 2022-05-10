import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#引入模块
import pymysql
import requests
import time
from bs4 import BeautifulSoup
import json
import re
import random
import logging
from lxml import etree

#设置日志
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#数据库连接方法
def get_db_conn():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           db='51job',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn
