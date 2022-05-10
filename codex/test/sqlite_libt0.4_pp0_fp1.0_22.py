import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import os.path
import sys
import re
import logging
import logging.handlers

# Python 2/3 compatibility
if sys.version_info[0] == 3:
    xrange = range
    unicode = str

# Python 2.6 compatibility
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

# Python 2.5 compatibility
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

# Python 2.4 compatibility
try:
    all
except NameError:
    def all(seq):
        for elem in seq:
            if not elem:
                return False
        return True

try:
    any
except NameError:
    def any(seq):
        for elem in seq:
            if elem:
                return True
        return False

# Python 2.3 compatibility
try:
    set
except NameError:
    from sets import Set as set

