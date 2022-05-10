import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import argparse
import json
import time
import datetime
import requests
import urllib
import re
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import quote
from urllib.parse import unquote
from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from
