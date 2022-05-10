import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import json
import random
import re
import requests
import threading
import logging
import logging.config
import logging.handlers
import traceback
import pymysql
import pymysql.cursors
import pymysql.err
import redis
import redis.exceptions

from bs4 import BeautifulSoup
from urllib.parse import quote

# 初始化日志
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("root")

# 初始化数据库连接
db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "db": "test",
    "charset": "utf8mb
