import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
import os
import sys
import time

import unittest
from test import support

# Skip test if _sqlite3 module not present.
support.import_module('_sqlite3')

SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101

SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_TEXT = 3
SQLITE_BLOB = 4
SQLITE_NULL = 5

SQLITE_STATIC = 0
SQLITE_TRANSIENT = -1

SQLITE_UTF8 = 1
SQLITE_UTF16 = 2
SQLITE_UTF16_BE = 3
SQLITE_UTF16_LE = 4
SQLITE_ANY = 5

SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2
SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5

