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
    return 1

def my_cb_auth(p):
    return 1

class MyThread(threading.Thread):
    def run(self):
        for i in range(100):
            my_threading_local.a.execute("SELECT test(1, 2)")

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(1))
lib.sqlite3_initialize()
lib.sqlite3_open_v2(DB_URI.encode("ascii"), ctypes.byref(my_threading_local.a), ctypes.c_int(1), None)
lib.sqlite3_set_authorizer(my_threading_local.a, my_cb_auth, None)
lib.sqlite3_set_busy_handler(my_threading_local.a, my_cb
