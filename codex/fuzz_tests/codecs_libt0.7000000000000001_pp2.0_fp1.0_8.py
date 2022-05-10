import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import re
import sys
import argparse
import json
import time
import pymysql
import datetime
import traceback
import subprocess
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import quote
from urllib.parse import unquote
from multiprocessing.dummy import Pool as ThreadPool
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("WARNING: install BeautifulSoup via pip install beautifulsoup4", file=sys.stderr)
    from BeautifulSoup import BeautifulSoup
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except ImportError:
    print("WARNING: install selenium via pip install selenium", file=sys.stderr)
try:
    from pyvirtualdisplay import Display
