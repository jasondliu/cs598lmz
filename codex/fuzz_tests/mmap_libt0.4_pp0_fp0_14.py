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

import common

def get_page_count(driver):
    page_count = driver.find_element_by_css_selector('div.pagination > span.pagination-info').text
    page_count = re.search(r'\d+', page_count).group(0)

    return int(page_count)

def get_page_content(driver):
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_page_urls(driver):
    soup = get_page_content(
