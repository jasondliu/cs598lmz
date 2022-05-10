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
    my_threading_local.a.close()
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

    sqlite3.enable_shared_cache(True)

    sqlite3.threadsafety = 0
    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.threadsafety
    sqlite3.paramstyle
    sqlite3.complete_statement("SELECT 1")
    sqlite3.complete_statement("SELECT 1;")
    sqlite3.complete_statement("SELECT 1; SELECT 2")
    sqlite3.complete_statement("SELECT 1; SELECT 2;")
    sqlite3.complete_statement("SELECT 1; SELECT 2; SELECT 3")
    sqlite3.complete_statement("SELECT 1; SELECT 2; SELECT 3;")
