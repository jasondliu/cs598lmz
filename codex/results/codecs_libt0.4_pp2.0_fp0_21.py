import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import os
import json
import re
import time
import datetime
import random
import logging
import logging.handlers
import requests
import urllib
import urllib.request
import urllib.parse
import urllib.error
import traceback
import http.cookiejar
import urllib.request, urllib.error, urllib.parse
import http.client
import socket

from bs4 import BeautifulSoup

import pymysql

# 设置默认编码为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# 日志设置
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s
