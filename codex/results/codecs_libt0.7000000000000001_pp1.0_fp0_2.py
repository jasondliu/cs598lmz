import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import logging
import requests
import logging.handlers

requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)

from utils import *
from common.models import *
from common.tools import *
from common.logger import *
from common.task import *
from common.conf import *

# 日志文件
logger = logging.getLogger()
LOG_FILE = '/data/bg_logs/s.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
formatter = logging.Formatter('%(asctime)s [
