import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import os
import sys
import re
import traceback
import platform
import warnings
import collections

# Python 3.x
try:
    import configparser
    from urllib.parse import unquote
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from urllib.parse import urlparse
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.error import URLError
# Python 2.x
except ImportError:
    import ConfigParser as configparser
    from urllib import unquote
    from urllib2 import urlopen
    from urllib import urlencode
    from urlparse import urlparse
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import URLError

# Python 2.x
try:
    text_type = unicode
# Python 3.x
except NameError:
    text_type = str

try:
    from cStringIO
