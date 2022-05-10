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

def my_complete_cb_with_error(user_data, error_message):
    print("my_complete_cb_with_error")

    return 0


def my_complete_cb(user_data, error_message):
    print("my_complete_cb")

    return 0


def my_progress_cb(user_data):
    print("my_progress_cb")
    return 0


def my_progress_cb_with_error(user_data):
    print("my_progress_cb_with_error")
    return 0

def my_row_cb(user_data):
    print("my_row_cb")

def my_row_cb_with_error(user_data):
    print("my_row_cb_with_error")

class A(ctypes.Structure):
    _fields_ = [('a', sqlite3_int64),
                ('b', ctypes.c_char_p)]


SQLITE3_NAME = ctypes.util.find_library("sqlite3")
SQLITE3 = c
