import mmap
import os
import pickle
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import traceback
import urllib
import urllib.parse
import urllib.request
import uuid
from queue import Queue
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from log_util import LogUtil
from util import Util
from util import get_config
from util import get_driver

logger = LogUtil.getLogger(__name__)

class WebDriver(object):

    def __init__(self, driver,
