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

def acallback(p, a, b):
    assert [a, b] == [1, 2]
    return 1

def acallback_exception(p, a, b):
    raise Exception("test")

def test_init():
    test.lib.sqlite3_initialize()
    test.lib.sqlite3_shutdown()

def test_thread():
    test.lib.sqlite3_initialize()
    test.lib.sqlite3_thread_cleanup()
    test.lib.sqlite3_shutdown()

def test_after_shutdown():
    test.lib.sqlite3_initialize()
    test.lib.sqlite3_shutdown()
    test.assert_raises(test.ProgrammingError, test.lib, "sqlite3_thread_cleanup")
