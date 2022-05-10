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
    b = my_threading_local.a

    b.cursor().execute("select test(1, 2)")
    b.close()

    return 1

def my_cb3(p):
    c = my_threading_local.a

    c.cursor().execute("select test(1, 2)")
    c.close()

    return 1

class my_thread(threading.Thread):
    def __init__(self, fn):
        threading.Thread.__init__(self)
        self.fn = fn

    def run(self):
        self.fn()

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)

    lib.sqlite3_initialize()

    lib.sqlite3_create_function(lib.sqlite3_db_handle(None), b"test", 2, lib.SQLITE_UTF8, None
