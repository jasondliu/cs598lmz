import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from BeautifulSoup import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pyvirtualdisplay import Display

from PIL import Image

from pprint import pprint

import logging

#logging.basicConfig(level=logging.DEBUG)

#logger = logging.getLogger(__name__)

import ConfigParser

import argparse


