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

def test_cb(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    return 1

def main():
    lib = ctypes.util.find_library("sqlite3")
    if not lib:
        raise Exception("Could not find sqlite3 library")
    lib = ctypes.CDLL(lib)
    lib.sqlite3_enable_load_extension(ctypes.c_int(1))
    lib.sqlite3_load_extension(ctypes.c_char_p(b"sqlite3"), ctypes.c_char_p(b"sqlite3_my_init"), ctypes.c_char_p(b"sqlite3_my_test"), ctypes.c_void_p())
    lib.sqlite3_enable_load_extension(ctypes.c_int(0))

    a = sqlite3.connect(DB_URI, uri=True)
    a.execute("select test(?, ?)", (1, 2))

