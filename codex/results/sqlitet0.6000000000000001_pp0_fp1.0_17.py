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

class MyTestCase(unittest.TestCase):
    def test_threading_local(self):
        # This test is only meant to be run to see if the leak happens.
        # It will leak if run, and the leak will not happen if the
        # offending code is commented out.
        #
        # The leak does not happen unless sqlite3_enable_shared_cache
        # is called.
        #
        # The leak does not happen if the callback is not used.
        #
        # The leak does not happen if the callback is called, but
        # the connection is not created.
        #
        # The leak does not happen if the connection is created, but
        # the function is not created.
        #
        # The leak does not happen if the function is created, but
        # the threading.local is not used.
        #
        # The leak does not happen if the threading.local is used, but
        # the function is not called.
        #
        # The leak does not happen if the function is called, but the
        # connection is not closed
