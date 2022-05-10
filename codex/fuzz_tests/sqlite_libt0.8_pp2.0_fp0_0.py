import ctypes
import ctypes.util
import threading
import sqlite3
import socket
import struct
import sys
import os
import time
import uuid

import common
import config
from common import ProtocolError
from urllib2 import URLError

LIB_CURL = ctypes.CDLL(ctypes.util.find_library('curl'), use_errno=True)

try:
    # All current versions of Python ship with sqlite3.
    # You'll need to install with pip or similar for Python 2.5.
    # The version in Ubuntu 8.04 (and presumably earlier) will lack
    # the necessary functionality.
    assert sqlite3.sqlite_version_info >= (3, 6, 0)
except (NameError, AssertionError):
    raise ImportError('Needs sqlite3 >= 3.6.0')

from sqlite3 import dbapi2 as sqlite

HTTP_PORT = 80
HTTPS_PORT = 443

class Error(Exception):
    """Base class of all errors."""

    def __init__(self, msg, cause=None):
        self.msg = msg
        self.
