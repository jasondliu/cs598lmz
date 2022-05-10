import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
import sys
import datetime
import requests
import json
import re
import time
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def run(crawl_date, crawl_time):
    print('Start:', crawl_date, crawl_time)
    if not os.path.exists(crawl_date):
        os.mkdir(crawl_date)
    if not os.path.exists(crawl_date + '/' + crawl_time):
        os.mkdir(crawl_date + '/' +
