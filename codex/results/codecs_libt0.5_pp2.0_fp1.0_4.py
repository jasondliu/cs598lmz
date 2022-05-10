import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import pymysql
import logging
import logging.handlers
import requests
import json
import re
import random
import uuid

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import configparser
import platform
import threading
import queue
import multiprocessing

# 获取日志文件信息
def get_logger(log_file):
    logger = logging.getLogger()
    formatter = logging.Formatter('
