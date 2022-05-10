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

def my_cb3(p):
    my_threading_local.a.cursor().execute("SELECT test(1, 2)")
    return 1

def test_callbacks():
    """
    This test is a bit of a hack.  It tests that callbacks are correctly
    registered and unregistered, and that the connection object is correctly
    deleted when the connection is closed.  It's a hack because it uses
    threading.local(), which is not guaranteed to work in a multi-threaded
    program.  However, it does work on Linux and Mac OS X.

    This test is also a bit of a cheat, because it relies on the fact that
    sqlite3.Connection objects are deleted when the connection is closed.
    This is not guaranteed by the Python interpreter.  However, it does work
    on Python 2.6.
    """
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(True)

