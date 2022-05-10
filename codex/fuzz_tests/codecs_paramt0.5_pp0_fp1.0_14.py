import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re
import os
import sys
import time
import datetime
import logging
import urllib
import urllib2

from pyquery import PyQuery

import config

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=config.LOG_FILE,
                    filemode='w')

class Base:
    def __init__(self):
        self.base_url = 'http://www.qidian.com'
        self.base_dir = config.BASE_DIR
        self.url = ''
        self.name = ''
        self.author = ''
        self.category = ''
        self.status = ''
        self.latest_chapter = ''
        self.latest_chapter_url = ''
        self.cover_url
