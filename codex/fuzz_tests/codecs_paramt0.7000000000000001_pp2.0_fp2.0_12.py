import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep

from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

import string
import re
import pandas as pd
import numpy as np
import json

import pickle
import os

from tqdm import tqdm

chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver

#from selenium.common
