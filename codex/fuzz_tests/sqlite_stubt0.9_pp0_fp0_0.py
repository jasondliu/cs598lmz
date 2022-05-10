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

def main():
    rc = sqlite3.SQLITE_OK

    try:
        sqlite3.enable_callback_tracebacks(True)
        cb = sqlite3.sqlite3_callback(my_cb)

        lib = ctypes.CDLL(ctypes.util.find_library("sqlite"))

        sqlite3_create_function_v2 = getattr(lib, 'sqlite3_create_function_v2')
        sqlite3_create_function_v2.restype = ctypes.c_int

        rc = sqlite3_create_function_v2(ctypes.c_voidp(), b"my callback", 1, ctypes.addressof(cb), None, None, None, None)
    finally:
        sqlite3.enable_callback_tracebacks(False)

    return rc

def sleep():
    delay = 10

    while True:
        print("Sleeping for {0} seconds".format(delay))
        time.sleep(delay)
        delay *= 1.2


def thread_func():

