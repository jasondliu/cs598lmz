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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
databasep = ctypes.c_char_p(DB_URI.encode('ascii'))

class MyThread(threading.Thread):
    def run(self):
        my_threading_local.func_ref = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

t = MyThread()
t.start()
t.join()

libsqlite3.sqlite3_open_v2(databasep, ctypes.byref(my_threading_local.a), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_CREATE, None)
libsqlite3.sqlite3_open_v2(databasep, ctypes.byref(my_threading_local.a), sqlite3.SQLITE_OPEN_READWR
