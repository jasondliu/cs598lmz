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
from bs4 import SoupStrainer

from lib import common
from lib import config
from lib import database
from lib import html_util
from lib import log
from lib import util

def get_url_from_file(file_name):
    """
    Reads a file and returns the first line.
    """
    with open(file_name, 'r') as f:
        return f.readline().strip()

def get_url_from_stdin():
    """
    Reads a URL from stdin.
    """
    return sys.stdin.readline().strip()

def get_url_from_clipboard():
    """
    Reads a URL from the clipboard.
    """
    return pyperclip.paste()

def get_url_from_browser():
    """
    Reads a URL from the browser.
    """
    # TODO: Implement this
