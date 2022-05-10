import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import base64
import json
import time
import datetime
import random
import requests
import sys
import os
import logging
import logging.handlers
import configparser
import pymysql
import pymysql.cursors
import traceback
import csv
import pprint

# from urllib.parse import quote

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException

