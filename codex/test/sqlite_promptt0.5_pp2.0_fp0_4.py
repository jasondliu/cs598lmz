import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('pragma journal_mode=wal').fetchone()

import platform

# Python 2/3 compatibility
try:
    import urllib.request as urllib
except ImportError:
    import urllib

# Python 3 compatibility
try:
    xrange
except NameError:
    xrange = range

# Python 3 compatibility
try:
    unicode
except NameError:
    unicode = str

# Python 3 compatibility
try:
    basestring
except NameError:
    basestring = str

# Python 3 compatibility
try:
    long
except NameError:
    long = int

# Python 3 compatibility
try:
    import queue
except ImportError:
    import Queue as queue

# Python 3 compatibility
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Python 3 compatibility
try:
    import http.client as httplib
except ImportError:
    import httplib

# Python 3 compatibility
