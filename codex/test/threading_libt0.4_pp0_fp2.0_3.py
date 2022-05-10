import threading
threading.Thread.daemon = True

import requests
import urllib
import json
import time
import os
import re
import sys
import datetime
import random
import math

from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import config

class InstagramScraper(object):

    def __init__(self, user_agent, cookie_file, tag, max_count):
        self.user_agent = user_agent
        self.cookie_file = cookie_file
        self.tag = tag
        self.max_count = max_count
        self.session = requests.Session()
        self.session.cookies = self.load_cookie()

    def load_cookie(self):
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'r') as f:
                cookie = requests.utils.cookiejar_from_dict(json.load(f))

