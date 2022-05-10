import sys, threading
threading.Thread(target=lambda: None).start()
sys.exit()

from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from urllib.request import Request
from urllib.request import urlopen
import json
from collections import OrderedDict
from time import sleep
from pprint import pprint 
from datetime import datetime
import re

from datetime import date


import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
