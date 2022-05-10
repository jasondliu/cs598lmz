import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections
import sqlite3.connections
# Test sqlite3.Cursor
import sqlite3.Cursor

import unittest
from test import test_support

SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101

# /usr/include/sqlite3.h:61
SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_TEXT = 3
SQLITE_BLOB = 4
SQLITE3_TEXT = 3

# /usr/include/sqlite3.h:66
SQLITE_UTF8 = 1
SQLITE_UTF16 = 2
SQLITE_UTF16_ALIGNED = 3

# /usr/include/sqlite3.h:95
SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2
SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6
SQL
