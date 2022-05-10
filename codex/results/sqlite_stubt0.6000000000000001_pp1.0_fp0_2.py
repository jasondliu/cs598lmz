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

class MyError(Exception):
    pass

def my_error_cb(p):
    raise MyError("My error")

def my_error_cb2(p):
    return 1

class UserError(Exception):
    pass

def my_user_error_cb(p):
    raise UserError("My user error")

def my_user_error_cb2(p):
    return 1

def my_bad_error_cb(p):
    raise ValueError("My bad error")

def my_bad_error_cb2(p):
    return 1

def my_bad_error_cb3(p):
    raise TypeError("My bad error")

def my_bad_error_cb4(p):
    raise KeyError("My bad error")

def my_bad_error_cb5(p):
    raise RuntimeError("My bad error")

def my_bad_error_cb6(p):
    raise AttributeError("My bad error")

def my_bad_error_cb7(p):
    raise Memory
