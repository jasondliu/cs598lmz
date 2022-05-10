import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import getopt
import re
import glob
import datetime
import shutil
import subprocess
import logging
import logging.handlers
import signal
import urllib2
import json
import socket

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/tmp/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

class NoResultError(Exception):
    pass

