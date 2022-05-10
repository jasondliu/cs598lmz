import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import sys
import json
import time
import random
import logging
import requests
import datetime

from bs4 import BeautifulSoup
from lxml import etree

from config import USER_AGENTS, URL_LIST, URL_LIST_2, MONGODB_CONFIG, MONGODB_CONFIG_2



class Proxy(object):
    def __init__(self):
        self.proxies = []
        self.urls = []
        self.logger = logging.getLogger(__name__)

    def get_proxies(self):
        """
        获取代理IP
        """
        for url in URL_LIST:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    self.logger.info(r.text)
                    ip_ports = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.
