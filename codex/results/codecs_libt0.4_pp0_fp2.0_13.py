import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import logging
import logging.config
import configparser
import argparse
import pymysql
import requests
import bs4
import re
import traceback
import random
import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import quote
from urllib.parse import unquote

class Crawler:
    def __init__(self, config, mode):
        self.config = config
        self.mode = mode
        self.logger = logging.getLogger(__name__)

        self.cnt = 0
        self.cnt_total = 0
        self.cnt_error = 0

        self.db = pymysql.connect(host=self.config.get('db', 'host'),
