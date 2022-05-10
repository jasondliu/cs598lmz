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

def multithreaded_init():
    _multithread = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    try:
        _multithread.sqlite3_config(3)
    except AttributeError:
        # you're on windows, 2nd argument ignored
        _multithread.sqlite3_config(3, 0)
    _multithread.sqlite3_initialize()
        # set up threadsafe callbacks
        # XXX do we need this on all threads?
    _multithread.sqlite3_config(7, 1)
        # register our callback
    # XXX we need to check for NULL ret here, but bpo-30551 may be a lie for
    # TODO the test_fn
    _multithread.sqlite3_auto_extension(my_cb)

if __name__ == '__main__':
    # initialize the DB
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute('create
