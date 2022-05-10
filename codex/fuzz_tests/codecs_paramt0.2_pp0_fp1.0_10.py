import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import json
import time
import datetime
import logging
import logging.handlers
import requests
import urllib
import urllib2
import urlparse
import argparse
import ConfigParser
import traceback

from bs4 import BeautifulSoup

from pymongo import MongoClient
from pymongo import errors as mongo_errors

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#
# Global variables
#

#
# Logging
#

logger = logging.getLogger('crawler')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('crawler.log', maxBytes=5*1024*1024, backupCount=5)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging
