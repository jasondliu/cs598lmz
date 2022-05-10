import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
import sys
import time
import logging
import logging.handlers
import json
import requests
from datetime import datetime
from optparse import OptionParser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from db import DB
from utils import Utils

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Scraper:
    def __init__(self):
        self.db = DB()
        self.utils = Utils()
        self.start_urls = []
        self.urls = []
       
