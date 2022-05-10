import codecs
codecs.register_error('ignore', codecs.ignore_errors)

import os
import re
import json
import requests
import urllib
import urllib2
import urlparse
import time
import hashlib
import random
import datetime
import cookielib
import logging
import traceback
import shutil
import threading
import Queue
import tempfile

from lxml import etree
from lxml.html import HTMLParser
from lxml.html import document_fromstring
from lxml.html import tostring

import settings

from utils import *

from logger import *

from db_utils import *

class BaseCrawler(object):
    """docstring for BaseCrawler"""

    name = 'base'
    copy_files = False
    headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/
