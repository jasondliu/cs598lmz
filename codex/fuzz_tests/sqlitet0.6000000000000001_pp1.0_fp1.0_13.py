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

def test_functions():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    assert a is my_threading_local.a
    a.execute("select test(1, 2)")
    del a

    try:
        from ctypes import util
        lib = ctypes.CDLL(util.find_library("sqlite3"))
    except:
        lib = ctypes.CDLL("libsqlite3.so")

    # This is a workaround for a bug in SQLite which can cause a segfault
    # when a destructor is called for a Python object that is being used
    # to implement a SQLite user-defined function.
    #
    # The workaround is to set the Python SQLite function implementation
    # to NULL before closing the database.
    #
    # See http://bugs.python.org/issue10740 for more details.
    py_sqlite_
