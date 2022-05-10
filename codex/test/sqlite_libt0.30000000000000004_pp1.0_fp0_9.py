import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re

from . import _sqlite3
from . import _sqlite3_ctypes

_sqlite3_version_info = _sqlite3.sqlite_version_info

if sys.version_info[0] >= 3:
    _string_types = str,
    _int_types = int,
    _range_type = range
    _text_type = str
    _binary_type = bytes
else:
    _string_types = basestring,
    _int_types = (int, long)
    _range_type = xrange
    _text_type = unicode
    _binary_type = str

def _check_remaining_sql(sql):
    """
    Checks that the string contains no characters other than whitespace
    after the SQL statement(s) have been parsed.
    """
