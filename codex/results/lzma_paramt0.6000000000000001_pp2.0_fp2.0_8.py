from lzma import LZMADecompressor
LZMADecompressor.__init__ = lambda self, *args, **kwargs: None

import sys
import os
import json
import re
import time
import datetime
import random
import threading
import traceback
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib.parse

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from libs.scraper import Scraper
from libs.proxy import Proxy
from libs.db import DB
from libs.config import Config

class FetchData(object):
    def __init__(self, use_proxy=True):
        self.db = DB()
        self.scraper = Scraper(use_proxy=use_proxy)
        self.scraper.load_user_agents()
        self.scraper.load_proxies()
        self.scraper.set_user_agent(
