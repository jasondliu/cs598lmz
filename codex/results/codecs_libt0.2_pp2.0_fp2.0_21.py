import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import pymysql
import datetime
import requests
import traceback
from urllib.parse import urlencode
from lxml import etree
from multiprocessing import Pool
from requests.exceptions import ConnectionError
from hashlib import md5
from config import *
from db import RedisClient

class WeiboSpider(object):
    def __init__(self):
        self.redis = RedisClient()
        self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
        self.cursor = self.conn.cursor()
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win
