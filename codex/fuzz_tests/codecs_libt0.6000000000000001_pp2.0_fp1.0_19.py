import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import sys
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

from pyvirtualdisplay import Display
from bs4 import BeautifulSoup

from urllib.request import urlopen
from urllib.request import urlretrieve

def get_url(url):
	html = urlopen(url)
	source = html.read()
	html.close()
	return source

def url_retrieve(url,path):
	urlretrieve(url,path)
