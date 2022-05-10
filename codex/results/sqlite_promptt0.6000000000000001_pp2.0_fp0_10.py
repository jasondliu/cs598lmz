import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import os
import sys

from . import _sqlite3 as sqlite3

# pysqlite_version is the version of the pysqlite module, not the underlying
# SQLite library.
from . import _version as pysqlite_version

from . import _sqlite3_ctypes as _sqlite3

from .dbapi2 import *

from .row import *

def _get_sqlite_func(db, f):
    """Return the address of the sqlite3 function named f"""
    if not isinstance(db, sqlite3.Connection):
        raise TypeError("db must be a sqlite3.Connection")
    dbver = db.sqlite_version_info
    if dbver < (3, 5, 0):
        raise NotImplementedError("sqlite3_load_extension requires SQLite 3.5.0 or later")
    return _sqlite3._sqlite3_get_function_address(db, f)

def _load_sqlite_functions(db, mod):
    """
