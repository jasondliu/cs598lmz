import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import time
import json
import datetime
import logging
import logging.handlers
import traceback

import requests
from bs4 import BeautifulSoup

import config
import db
import util

logger = logging.getLogger(__name__)

def get_html(url):
    logger.debug('get_html: url=%s', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.text

def get_soup(url):
    logger.debug('get_soup: url=%s', url)
    html = get_html(url)
    return BeautifulSoup(html, 'html.parser')

def get_soup_from_file
