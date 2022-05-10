import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html#threading-daemon-threads
from threading import Thread
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import time, sleep
from random import randint, random
import pandas as pd
from tqdm import tqdm_notebook
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
# selenium can't set attribute for protected elements
# https://stackoverflow.com/questions/13249409/selenium-webdriver-in-python-cant-set-attribute-for-protected-elements
from selenium
