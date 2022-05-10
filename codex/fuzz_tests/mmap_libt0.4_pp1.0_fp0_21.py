import mmap
import os
import re
import sys
import time
from functools import wraps
from io import BytesIO
from multiprocessing import Process
from multiprocessing.pool import ThreadPool
from threading import Thread

from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import logger
from .config import Config
from .exceptions import (
    CaptchaException,
    LoginException,
    NoSuchElementException,
    NoSuchUserException,
    PrivateAccountException,
    RetryLimitException,
    ServerErrorException,
    TooManyRequestsException,

