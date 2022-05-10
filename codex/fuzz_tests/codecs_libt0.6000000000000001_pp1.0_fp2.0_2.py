import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import os
import datetime
import re

from pymongo import MongoClient
from dateutil.parser import parse

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

from util import *

def crawl_news(crwal_date):
    print("crawling news from: " + crwal_date.strftime('%Y-%m-%d'))
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    browser.get("https://www.google.com/search?q=site%3Ahttp%3A%2F%2Fwww.finance.gov.tw%2Fch%2Fhome%2Fnews%2Fnews00.aspx&tbs=qdr:d")
    time.sleep(2)
    elem = browser.find_element_by_xpath("
