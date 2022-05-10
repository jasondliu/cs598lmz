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

def test_thread():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_ReleaseThread(ctypes.pythonapi.PyEval_SaveThread())

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_shutdown()
    lib.sqlite3_config(
        ctypes.c_int(4), # SQLITE_CONFIG_MULTITHREAD
        ctypes.c_int(1), # SQLITE_CONFIG_SINGLETHREAD
    )
    lib.sqlite3_initialize()

    lib.sqlite3_initialize()

    lib.sqlite3_config(
        ctypes.c_int(4), # SQLITE_CONFIG_MULTITHREAD
        ctypes.c_int(1), # SQLITE_CONFIG_SINGLETHREAD
    )

    lib.sql
