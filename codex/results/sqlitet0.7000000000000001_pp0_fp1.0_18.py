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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_shutdown()
ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(2), my_cb)
ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_initialize()

# This test fails, as the connection is closed before the thread is joined.
# However, it was written for the initial patch which would close the connection
# after the thread was joined.
#
# Thread 1 has the connection in its thread-local.
# Thread 2 tries to allocate the same connection, but it's already in use.
# The test fails iff the connection is closed when this happens.

def f(r):
    r[0] = my_threading_local.a.execute("select test(1, 2)").fetchall()

r = [None]

t = threading.Thread(target=f, args=(r,))
t.start()

