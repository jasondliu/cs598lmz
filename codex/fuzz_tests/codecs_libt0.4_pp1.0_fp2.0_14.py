import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import os
import re
import time
import datetime
import json
import requests
import random
import string
import urllib
import urllib2
import cookielib
import threading
import Queue
import sqlite3
import logging
from bs4 import BeautifulSoup


# 日志
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='logs/' + time.strftime("%Y-%m-%d", time.localtime()) + '.log',
                filemode='a')

# 初始化

#
