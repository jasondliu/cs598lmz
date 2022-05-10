import ctypes
ctypes.cast(None, ctypes.c_void_p)

from datetime import datetime
import pytz
from pytz import timezone
import time
from bs4 import BeautifulSoup as bs
import requests
from urllib.parse import urljoin
import re
from requests import get
import json
import configparser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.utils import ChromeType
from webdriver_manager.driver import ChromeDriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
