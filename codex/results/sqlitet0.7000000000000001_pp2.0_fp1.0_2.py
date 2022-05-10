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

def my_cb3(p):
    return sqlite3.connect(DB_URI, uri=True, factory=deleting_conn).create_function("test", 2, lambda a,b: a)

def run_sql(sql):
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    return conn.execute(sql).fetchall()

def test_cb_init():
    lib = ctypes.CDLL(ctypes.util.find_library(ctypes.util.find_library('sqlite3')))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

    lib.sqlite3_enable_shared_cache(ctypes.c_int(1))

    lib.sqlite3_config(ctypes.c_int(42), ctypes.py_object(my_cb))
    lib.sqlite3_initialize()

    assert run_sql("
