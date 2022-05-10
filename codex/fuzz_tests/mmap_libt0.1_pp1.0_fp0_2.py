import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import *

def get_page_source(driver, url):
    driver.get(url)
    return driver.page_source

def get_page_source_with_retry(driver, url, retry_count=3):
    for i in range(retry_count):
        try:
            return get_page_source(driver, url)
        except Exception as e:
            print 'Error: %s' % e
            print 'Retry %d/%d' % (i+1, retry_count)
            time.sleep(1)
    return None


