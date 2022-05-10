import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select
import time
import os
import re
import sys
import json
import datetime
import random
import urllib.parse
import pymysql

import logging
from logging import handlers
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import threading

# 全局变量
# 数据库
