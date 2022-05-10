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

class CustomDllLoader(object):
    def __init__(self, dll):
        self.dll = dll

    def __call__(self, dll_path):
        if dll_path == self.dll:
            return ctypes.CDLL(dll_path)
        else:
            return None

def my_init():
    ctypes.CDLL(ctypes.util.find_library("sqlite3"),
                ctypes.RTLD_GLOBAL)

    ctypes.CDLL(ctypes.util.find_library("c"),
                ctypes.RTLD_GLOBAL)

    ctypes.CDLL(ctypes.util.find_library("m"),
                ctypes.RTLD_GLOBAL)

    ctypes.CDLL(ctypes.util.find_library("pthread"),
                ctypes.RTLD_GLOBAL)

    ctypes.util.find_library = CustomDllLoader("libc.so.6")

    sqlite3.sqlite_version_info = (3,8,11)

