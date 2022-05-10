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

def my_cb_proxy(p):
    return my_cb(p)

def my_cb_proxy_proxy(p):
    return my_cb_proxy(p)

def my_cb_proxy_proxy_proxy(p):
    return my_cb_proxy_proxy(p)

class test():
    def __init__(self):
        self.conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        self.conn.set_authorizer(my_cb_proxy_proxy_proxy)

    def __del__(self):
        self.conn.close()

def test_fn(a, b):
    return a

def my_cb_2(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_cb_proxy_2(p):
    return my
