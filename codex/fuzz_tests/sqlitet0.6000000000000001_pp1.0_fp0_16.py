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

def my_thread():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_SaveThread()

    my_threading_local.a.execute("select test(?, ?)", (5, 6))
    my_threading_local.a.commit()

libsqlite3 = ctypes.util.find_library("sqlite3")
if not libsqlite3:
    raise RuntimeError("Failed to find sqlite3 library")

lib = ctypes.CDLL(libsqlite3)

lib.sqlite3_set_authorizer(None, my_cb)

t = threading.Thread(target=my_thread)
t.start()
t.join()
</code>

