import threading
# Test threading daemon
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import *
from utils import *


class Scrapper():
    def __init__(self, url, driver_path, headless=True):
        self.url = url
        self.driver_path = driver_path
        self.headless = headless
        self.driver = None
        self.soup = None

    def get_html(self):
        if self.headless:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(self.driver_path, options=options)
        else:
            self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        self.driver.close()


class ThreadScrapper(Scrapper, threading.Thread
