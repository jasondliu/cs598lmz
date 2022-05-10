import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import json
import re
import random
import requests
import threading
import traceback
import pymysql
import pymongo
import redis
import logging
import logging.handlers
import logging.config

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from collections import OrderedDict
from pymongo import MongoClient
from pymongo import ASCENDING
from pymongo import DESCENDING
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver
