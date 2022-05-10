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

def test_cb():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyThreadState_New.restype = ctypes.py_object

    libsqlite = ctypes.util.find_library('sqlite3')
    if not libsqlite:
        return

    libsqlite = ctypes.CDLL(libsqlite)
    libsqlite.sqlite3_enable_shared_cache(True)

    my_cb_func = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    libsqlite.sqlite3_auto_extension(my_cb_func)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = conn.cursor()

    cur.execute("SELECT test(?)", (1,))
    assert cur.fetchone()[0] == 1

    cur = my_threading_local.a.cursor()
    cur.execute("SELECT test(?)", (1,))
