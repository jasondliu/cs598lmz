import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_ste_cb(p):
    return 1

def my_op_cb(p):
    return 1

def my_cp_cb(p):
    return 1

from ctypes import c_int
SQLITE_OK = 0
SQLITE_UTF8 = 1
SQLITE_DETERMINISTIC = 0x800

SQLITE_INTERNAL = 2
SQLITE_MISUSE = 21
SQLITE_ROW = 100
SQLITE_DONE = 101

busy_handler = sqlite3.SQLiteBusyHandler()
thread_hooks = sqlite3.SQLiteThreadHook()

if hasattr(ctypes, "c_void_p"):
    SQLITE_TRANSIENT = ctypes.c_void_p(-1)
else:
    SQLITE_TRANSIENT = ctypes.c_int(-1)

class TestSqlite3u(unittest.TestCase):
    def test_basic(self):
        a = sqlite3.connect(DB_URI, uri=True
