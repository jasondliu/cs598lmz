import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
#import urllib
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import re

def main():
    #'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' - 要查看
    driver = webdriver.Chrome()

    #打開pchome螢幕大小頁面
    url_home = 'http://24h.pchome.com.tw'
    url_
