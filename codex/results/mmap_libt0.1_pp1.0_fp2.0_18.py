import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import config
from . import db
from . import util

def get_page(url, data=None, headers={}, timeout=None):
    """
    Get a page from the web.
    """
    if timeout is None:
        timeout = config.getint('web', 'timeout')
    if data is not None:
        data = urllib.urlencode(data)
    request = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(request, timeout=timeout)
    except urllib2.HTTPError as e:
        if e.code == 404:
            raise util.NotFoundError(url)
        else:
            raise
    return response.read()

def get_soup(url, data=None, headers={}, timeout=None):
    """
    Get a BeautifulSoup object from a
