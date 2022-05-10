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

def main():
    ctypes.pythonapi.PyEval_InitThreads()
    p = ctypes.POINTER(ctypes.c_int)()
    ctypes.pythonapi.PyEval_SaveThread(p)
    ctypes.pythonapi.PyEval_RestoreThread(p)
    ctypes.pythonapi.PyEval_ReleaseThread(p)
    ctypes.pythonapi.PyEval_AcquireThread(p)
    ctypes.pythonapi.PyEval_ReInitThreads()

    sqlite3.threadsafety = 1
    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    sqlite3.create_function("test", 2, test_fn)

    t = threading.Thread(target=my_cb, args=(p,))
    t.start()
    t.join()

    a = my_threading_local.a

    a.execute("SELECT test(1, 2)")
    a
