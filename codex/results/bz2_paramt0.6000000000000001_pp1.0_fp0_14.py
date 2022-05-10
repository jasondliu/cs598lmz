from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: data

from bz2 import BZ2File
BZ2File.read = lambda self, size=None: self.readline()

import pytz
from pytz import timezone
timezone = timezone('US/Eastern')

from datetime import datetime
import time
from time import mktime
import pycurl
from StringIO import StringIO

import requests
from requests import get

from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests.auth import AuthBase

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from lxml import html
from lxml import etree
from lxml.cssselect import CSSSelector
from lxml.etree import tostring
from lxml.html import fromstring
from lxml.html import tostring

from cssselect import GenericTranslator
from cssselect import SelectorSyntaxError

from ast import literal_eval

