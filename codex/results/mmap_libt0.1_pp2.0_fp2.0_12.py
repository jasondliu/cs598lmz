import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import *

# TODO:
# - Add support for multiple pages
# - Add support for multiple search terms
# - Add support for multiple search engines
# - Add support for multiple search engines per search term
# - Add support for multiple search engines per search term per page
# - Add support for multiple search engines per search term per page per search
# - Add support for multiple search engines per search term per page per search per result
# - Add support for multiple search engines per search term per page per search per result per link
