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

def my_callback(p):
    return 1;

def my_callback_with_arg(p, arg):
    return 1;

def my_callback_with_kwargs(p, kwargs):
    return 1;

def my_callback_with_args(p, *args):
    return 1;

def my_callback_with_args_and_kwargs(p, *args, **kwargs):
    return 1;

def my_callback_with_bad_args(p, **kwargs):
    return 1;

def my_callback_with_bad_args2(p, *args, **kwargs):
    return 1;

def my_callback_with_bad_args3(p):
    return 1;

def test_threading():
    if sys.platform == "win32":
        return
    p = ctypes.create_string_buffer(b"test")

    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_
