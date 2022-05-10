import mmap
import random
import re
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import utils


class Scraper:
    def __init__(self,
                 username,
                 password,
                 headless=True,
                 download_path=None,
                 random_user_agent=True,
                 random_proxy=True,
                 proxy_file=None,
                 proxy_user=None,
                 proxy_pass=None,
                 proxy_port=None):
        self.username = username
        self.password = password
        self.headless = headless
        self.download_path = download_path
        self.random_user_agent = random_user_agent
        self.random_proxy = random_proxy
        self.proxy_file = proxy
