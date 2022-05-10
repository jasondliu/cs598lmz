import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import requests
import random
import datetime
import threading
import traceback
import Queue
import logging
import logging.handlers

from bs4 import BeautifulSoup

from config import *
from utils import *
from db import *
from proxy import *
from logger import *
from exception import *

class Crawler(object):
    def __init__(self, url, logger, proxy_queue, db, lock):
        self.url = url
        self.logger = logger
        self.proxy_queue = proxy_queue
        self.db = db
        self.lock = lock
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-
