import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import os
import sys
import platform
from warnings import warn

from . import _sqlite3
from . import _version as sqlite_version
from .dbapi2 import *

from . import _sqlite3

version_info = sqlite_version.version_info
sqlite_version = sqlite_version.sqlite_version
sqlite_version_info = sqlite_version.sqlite_version_info

PARSE_COLNAMES = _sqlite3.PARSE_COLNAMES
PARSE_DECLTYPES = _sqlite3.PARSE_DECLTYPES

# constants used with the detect_types parameter to connect()
PARSE_DECLTYPES = _sqlite3.PARSE_DECLTYPES
PARSE_COLNAMES = _sqlite3.PARSE_COLNAMES

#------------------------------------------------------------------------------
# Exception hierarchy. DB-API 2.0 specifies a base Exception but does not
# require implementations to derive all exceptions from it.
#

class Warning(Exception):
    pass

class Error(Exception
