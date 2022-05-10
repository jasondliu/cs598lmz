import codecs
codecs.register_error('ignore', codecs.ignore_errors)

import os
import sys
import re
import json
import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

ua = UserAgent()

def get_html(url):
    headers = {'User-Agent': ua.random}
    r = requests.get(url, headers=headers)
    return r.text

def get_soup(
