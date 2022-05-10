import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import re
import os
import sys
import csv
import json
import datetime
import random

import requests
from bs4 import BeautifulSoup

import smtplib
from email.mime.text import MIMEText

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.options import Options

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %
