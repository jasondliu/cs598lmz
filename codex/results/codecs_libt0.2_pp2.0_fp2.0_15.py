import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import random
import threading
import traceback
import logging
import logging.config

import requests
from requests.exceptions import ConnectionError

from config import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

class Weibo(object):
    def __init__(self, config):
        """ Weibo类初始化 """
        self.validate_config(config)
        self.filter = config[filter]
        self.since_date = config[since_date]
        self.write_mode = config[write_mode]
        self.pic_download = config[pic_download]
        self.video_download = config[video_download]
        self.mysql_config = config[mysql_config]
        self.redis_config = config[redis_config]
        self
