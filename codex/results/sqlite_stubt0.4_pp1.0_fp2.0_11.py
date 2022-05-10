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
    ctypes.pythonapi.PyEval_ReleaseLock()
    ctypes.pythonapi.PyEval_AcquireLock()

    sqlite3.sqlite_version_info
    sqlite3.threadsafety
    sqlite3.sqlite_version

    p = sqlite3.sqlite_version_info
    ctypes.pythonapi.PyEval_ReleaseLock()

    p = ctypes.pythonapi.PyEval_SaveThread()

    ctypes.pythonapi.PyEval_AcquireThread(p)

    ctypes.pythonapi.PyEval_ReleaseThread(p)

    sqlite3.sqlite_version_info

    sqlite3.threadsafety
    sqlite3.sqlite_version

    ctypes.pythonapi.PyEval_AcquireThread(p)

    ctypes.pythonapi.PyEval_ReleaseLock()

    ctypes.pythonapi.PyEval_AcquireLock()

    ctypes.pythonapi.PyEval_Release
