import threading
threading.stack_size(67108864)

import logging
logging.basicConfig(level=logging.DEBUG)

#set up log file
logging.basicConfig(filename='coke.log',level=logging.DEBUG)

import os
import sys

import json
import time
import datetime
import pytz

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# set Chrome options
options = Options()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1366x768')

# set the window size
options.add_argument('window-size=1200x600')

# initialize driver
#
