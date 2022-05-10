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

def test_init_conn():
    p = ctypes.POINTER(ctypes.c_int)()
    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)
    sqlite3.sqlite3_set_authorizer(p, my_cb, None)
    sqlite3.sqlite3_close(p)

def test_init_conn_concur():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=test_init_conn))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def test_init_conn_crash():
    p = ctypes.POINTER(ctypes.c_int)()
    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p), sqlite3.SQLITE_
