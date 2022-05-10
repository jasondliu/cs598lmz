import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

from google.appengine.ext import db

import logging
_logger = logging.getLogger("sqlite3")
_logger.setLevel(logging.DEBUG)
_debug_logger = logging.FileHandler("sqlite.log")
_logger.addHandler(_debug_logger)

class RuntimeException(Exception):
    pass

# Check that s is an sqlite3.sqlite_base.Cursor object.
def is_sqlite_cursor(s):
    return s is not None and s.__class__.__name__ == "Cursor"

# Check that s is an sqlite3.sqlite_base.Connection object.
def is_sqlite_connection(s):
    return s is not None and s.__class__.__name__ == "Connection"

# Returns the sqlite dll path.
def get_sqlite_dll_path():
    dlls = ["libsqlite3-0.dll", "libsqlite3.dll"]
