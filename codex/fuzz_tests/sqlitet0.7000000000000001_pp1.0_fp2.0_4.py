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

class MyException(Exception):
    pass

def my_exception_handler(type, value, traceback):
    raise MyException(value)

def main():
    old_hook = sys.excepthook
    sys.excepthook = my_exception_handler
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_threadsafe()
    libsqlite3.sqlite3_config(ctypes.c_int(4))
    libsqlite3.sqlite3_initialize()
    libsqlite3.sqlite3_create_function(0, b"test", 2, 1, 0, 0, 0)
    libsqlite3.sqlite3_auto_extension(my_cb)
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("select test(?);", (1,))
    a.close()
    libsqlite3.sqlite
