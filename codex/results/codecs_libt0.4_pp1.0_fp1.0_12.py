import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import pymysql
import requests
import datetime
import traceback
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WeiboSpider():
    def __init__(self):
        self.url = 'https://s.weibo.com/weibo?q={}&Refer=SWeibo_box&page={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (
