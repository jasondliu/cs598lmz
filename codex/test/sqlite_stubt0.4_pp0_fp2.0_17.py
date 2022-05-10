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
    del my_threading_local.a
    return 1

def main():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_ReleaseLock()

    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(3, 1)
    lib.sqlite3_initialize()

    lib.sqlite3_config(7, my_cb, my_cb2, None)

    db = sqlite3.connect(DB_URI, uri=True)
    db.execute("create table test (a, b)")
    db.execute("insert into test values (1, 2)")
    db.execute("insert into test values (3, 4)")
    db.execute("select test(a, b) from test")
