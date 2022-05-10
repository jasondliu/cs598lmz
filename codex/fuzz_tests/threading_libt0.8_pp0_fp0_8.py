import threading
threading.stack_size(2**27) 
# Increase stack size to let BeautifoulSoup parse HTML
import html5lib 
from urllib2 import urlopen
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib2
import codecs
from urllib2 import Request, urlopen, URLError
import re
from random import randint
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import httplib
from urllib import urlencode
def initialise_selenium():
    global fp
    global driver
    global wait
    
    
    fp = webdriver.FirefoxProfile() 
    fp.set_preference("browser.privatebrowsing.autostart", True
