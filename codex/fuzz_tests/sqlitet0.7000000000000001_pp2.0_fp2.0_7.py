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

def test_set_authorizer():
    # the test_set_authorizer is called in a way that is not thread safe
    # in e.g. Python 3.4.3 and sqlite3 versions < 3.8.3.1
    #
    # this is because the test uses a shared sqlite3.Connection object
    # which is not thread safe:
    # https://docs.python.org/2/library/sqlite3.html#using-the-connection-as-a-context-manager
    #
    # this test demonstrates that using the context manager feature
    # of sqlite3.Connection will not fix the problem: the context manager
    # feature uses a shared sqlite3.Connection object as well.
    #
    # this test tries to reproduce the problem:
    # - 2 threads are started with each a my_cb callback
    # - my_cb gets the shared sqlite3.Connection object
    # - the two threads share this connection object
    # - the first thread will try to create a sqlite3.Connection object
    #   inside the my_cb function
   
