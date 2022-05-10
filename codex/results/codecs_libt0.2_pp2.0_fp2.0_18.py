import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import logging
import traceback
import requests
import random
import re
import string
import urllib
import urllib2
import urlparse
import cookielib
import base64
import hashlib
import hmac
import binascii
import threading
import Queue
import MySQLdb
import MySQLdb.cursors

from lxml import etree
from lxml.cssselect import CSSSelector

import config

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log/%s.log' % (time.strftime('%Y-%m-%d')),
                    filemode='a
