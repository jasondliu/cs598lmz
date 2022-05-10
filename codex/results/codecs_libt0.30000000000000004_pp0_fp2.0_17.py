import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import datetime
import time
import re
import random
import string
import logging
import traceback
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pymysql
import pymysql.cursors

import config

# 连接数据库
def connect_db():
    connection = pymysql.connect(host=config.DB_HOST,
                                 user=config.DB_USER,
                                 password=config.DB_PASSWORD,
                                 db=config.DB_DATABASE,
                                 charset=config.DB_CHARS
