import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import os
import re
import time
import json
import random
import datetime
import threading
import traceback
import multiprocessing as mp

import requests
import pymongo

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gg_utils import get_logger, get_proxy, get_user_agent

logger = get_logger(__name__)

# 全局设置
# 是否使用代理
use_proxy = True
# 是否使用高匿代理
use_anonymity_proxy = True
#
