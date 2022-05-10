import ctypes
import ctypes.util
import threading
import sqlite3
import MySQLdb
import redis
import urllib
import urllib2
import requests
import httplib2
import html2text
import tempfile
import hashlib
import base64
import zlib
import json
import difflib
import subprocess
import shlex

from PIL import Image
from cStringIO import StringIO
from cgi import escape
from BeautifulSoup import BeautifulSoup, Tag
from distutils.version import LooseVersion, StrictVersion
from StringIO import StringIO
from time import time as timefunc
from log import logger

try:
    import magic
except importError, e:
    magic = None

try:
    import json
except ImportError:
    import simplejson as json


def timeit(method):
    def timed(*args, **kw):
        ts = timefunc()
        result = method(*args, **kw)
        te = timefunc()
        logger.debug('%r %2.2f sec' % (method.__name__, te-ts))
        return result
    return timed


MUST_INCL
