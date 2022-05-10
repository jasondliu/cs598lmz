import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

from ctypes import *
from ctypes.util import find_library

from sqlite3_api import *
from sqlite3_dbapi2 import *

if sys.platform == "win32":
    sqlite3 = ctypes.windll.sqlite3
else:
    sqlite3 = cdll.LoadLibrary(find_library("sqlite3"))

test_connection = None
test_cursor = None

def setup_module():
    global test_connection
    global test_cursor
    test_connection = sqlite3.connect(":memory:")
    test_cursor = test_connection.cursor()

def teardown_module():
    global test_connection
    global test_cursor
    test_connection.close()

def build_row_factory_test():
    from sqlite3_dbapi2 import Row
    test_cursor.execute("create table test(a, b, c)")
