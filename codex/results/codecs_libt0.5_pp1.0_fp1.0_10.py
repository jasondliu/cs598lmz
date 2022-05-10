import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import random
import copy
import json
import re
import MySQLdb
import requests
import urllib
import urllib2
import urlparse
import cookielib
import traceback
import logging
import logging.handlers
from bs4 import BeautifulSoup

# from config import *

reload(sys)
sys.setdefaultencoding('utf8')

# 全局变量
g_host = 'localhost'
g_user = 'root'
g_passwd = 'root'
g_db = 'wuyou'

g_conn = MySQLdb.connect(host=g_host, user=g_user, passwd=g_passwd, db=g_db, charset='utf8')
g_cursor = g_conn.cursor()

# 日志
g_logger = logging.getLogger('mylogger')
