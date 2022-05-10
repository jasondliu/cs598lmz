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

def my_cb_final(p):
    my_threading_local.a.close()
    del my_threading_local.a

    return 1

def get_conn():
    return my_threading_local.a

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

def initialize_sqlite3():
    lib.sqlite3_initialize()
    lib.sqlite3_config(2, 1)

def shutdown_sqlite3():
    lib.sqlite3_shutdown()

class my_pool:
    def __init__(self):
        self.pool = []
        while len(self.pool) < 20:
            self.pool.append(None)
        self.lock = threading.Lock()

    def get_conn(self):
        self.lock.acquire()
        c = self.pool.pop()
        self.lock.release()
        return c

    def put_conn(self, c):
        self.lock.acquire()
        self.pool
