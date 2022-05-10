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

def test_init():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_initialize()

def test_thread_init():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(2), my_cb, my_cb2, 0)

def test_thread_init_fail():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(2), my_cb, my_cb2, 0)

def test_thread_init_fail2():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(2), my_cb, my_cb2, 0)

def test_thread_init_fail3():
    ctypes
