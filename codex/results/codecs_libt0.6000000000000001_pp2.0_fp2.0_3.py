import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import pandas as pd
import numpy as np
import re
import os

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

from datetime import datetime
from dateutil.parser import parse

import time
from time import sleep

import json

def get_soup(url):
    sleep(np.random.randint(1,10))
    headers = {'User-Agent': 'Mozilla/5.0 (
