import mmap
# Test mmap.mmap class
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile
from zlib import compress
from pickle import dump, load
from struct import unpack, pack
import re
from os import walk
from functools import wraps
from time import time
from os.path import sep, getsize, basename, join, normpath, exists, dirname
from collections import OrderedDict
import sys
from os import remove
from random import randrange
from math import log, ceil
import argparse

from logger import Logger
from config import Configuration
from analyzer import Analyzer


logger = Logger(__name__)

try:
    from ConfigParser import ConfigParser  # Python 2.7
except ImportError:
    from configparser import ConfigParser  # Python 3.4

config = ConfigParser()
config.read('config.ini.default')
config.read('config.ini')

# Python 2.7
try:
    from urllib import quote_plus, unquote
    from urllib2 import urlopen, URLError, HTTP
