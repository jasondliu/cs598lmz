import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
from bs4 import BeautifulSoup

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from collections import defaultdict
from pymongo import MongoClient
import json
from pprint import pprint

from selenium.webdriver.chrome.options import Options

from bson.objectid import ObjectId

from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium.web
