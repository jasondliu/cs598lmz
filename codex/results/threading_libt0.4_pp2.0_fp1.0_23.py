import threading
threading.Thread(target=lambda: None).start()

import time
import sys
import os
import json
import requests
import pymongo
import datetime
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


# 오늘 날짜
now = datetime.datetime.now()
nowDate = '{0:%Y-%m-%d %H:%M:%S}'.format(now)

# 크롬 옵
