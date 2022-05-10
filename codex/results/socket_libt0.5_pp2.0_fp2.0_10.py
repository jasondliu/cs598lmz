import socket
import sys
import os
import time
import re
from datetime import datetime
import json
import subprocess
import requests
from requests.exceptions import ConnectionError

#from lxml import etree
#from lxml import html

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.action_chains import ActionChains

import selenium.common.exceptions as selenium_exceptions

import threading

#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.proxy import Proxy, ProxyType

import
