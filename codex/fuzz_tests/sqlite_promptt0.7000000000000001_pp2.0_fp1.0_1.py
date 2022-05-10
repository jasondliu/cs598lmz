import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
import datetime
import types
import os.path
import os
import re
from types import MethodType
import sys

# Setup Logging #
import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger('pytrainer')

# Setup for i18n
import gettext
from gettext import gettext as _
gettext.textdomain('pytrainer')
try:
    gettext.bindtextdomain('pytrainer',os.path.join(os.path.dirname(__file__),'locale'))
except:
    print >> sys.stderr, "Locale not found, using default"
    gettext.bindtextdomain('pytrainer','locale')
import __builtin__
__builtin__.__dict__['_'] = _
#End setup #

class DBUtils:
    def __init__(self, parent = None):
        self._parent = parent
