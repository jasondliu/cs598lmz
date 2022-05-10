import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

import pymysql
import pandas as pd
import numpy as np
import re
import time
import datetime
import json
import requests
import logging
from logging.handlers import RotatingFileHandler
from sqlalchemy import create_engine
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)

