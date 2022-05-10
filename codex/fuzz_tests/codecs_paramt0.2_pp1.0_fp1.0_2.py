import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import time
import datetime
import json
import logging
import logging.handlers
import traceback
import requests
import urllib
import urllib2
import urlparse
import cookielib
import random
import string
import hashlib
import base64
import hmac
import binascii
import threading
import Queue
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from requests.packages.urllib3.exceptions import InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

from requests.packages.urllib3.exceptions import SNIMissingWarning
requests.packages.urllib3.disable_warnings(SNIMissingWarning)

from requests.
