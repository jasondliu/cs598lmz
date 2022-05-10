import mmap
import os
import re
import sys
import time
import traceback
import urllib

try:
    import json
except ImportError:
    import simplejson as json

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

try:
    import requests
except ImportError:
    requests = None

try:
    import bs4
except ImportError:
    bs4 = None

try:
    import pycurl
except ImportError:
    pycurl = None

try:
    import magic
except ImportError:
    magic = None

try:
    import pymongo
except ImportError:
    pymongo = None

try:
    import MySQLdb
except ImportError:
    MySQLdb = None

try:
    import pymysql
except ImportError:
    pymysql = None

try:
    import psycopg2
except Import
