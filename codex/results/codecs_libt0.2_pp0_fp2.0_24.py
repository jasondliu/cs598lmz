import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import random
import requests
import threading
import traceback

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

from pymongo import MongoClient

from config import *

class Weibo:
    def __init__(self, user_id, filter=0):
        """Weibo类初始化"""
        if user_id.isdigit():
            self.user_id = user_id
        else:
            sys.exit(u"user_id值
