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

def my_cb2(p):
    return 1

def main():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table tbl(a int)")

    sqlite3.sqlite3_open = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True).sqlite3_open

    sqlite3.sqlite3_open_v2 = ctypes.CDLL(ctypes.util.find_library(
        'sqlite3'), use_errno=True).sqlite3_open_v2

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb2)

    sqlite3.sqlite3_config(sqlite3.
