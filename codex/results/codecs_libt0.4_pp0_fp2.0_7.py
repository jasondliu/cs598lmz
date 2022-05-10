import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import traceback
import pymysql
import logging
import logging.handlers
import argparse
import ConfigParser
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

g_logger = None
g_config = None
g_db = None

def init_logger(log_path, log_name):
    global g_logger
    if g_logger is not None:
        return
    g_logger = logging.getLogger(log_name)
    g_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    file_handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=1024 * 1024 * 10, backupCount=10)
