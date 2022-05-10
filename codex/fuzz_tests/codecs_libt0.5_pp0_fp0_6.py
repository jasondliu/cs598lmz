import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import random
import sys
import os
import time
import datetime
# import json
import pymysql
import pymysql.cursors
import pandas as pd
from sqlalchemy import create_engine

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulS
