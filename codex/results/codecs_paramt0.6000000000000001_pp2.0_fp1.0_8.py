import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Import the required modules.
import argparse, os, re, sys, requests, json

# Import the required modules.
from bs4 import BeautifulSoup
from time import sleep

# Import the required modules.
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the required modules.
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.opera.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# Import the required modules.
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

# Import the
