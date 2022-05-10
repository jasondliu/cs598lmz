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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_open(DB_URI.encode('utf-8'), ctypes.byref(my_threading_local.db))
lib.sqlite3_exec(my_threading_local.db, "CREATE TABLE a(x)", None, None, ctypes.byref(my_threading_local.err))
lib.sqlite3_exec(my_threading_local.db, "INSERT INTO a VALUES (1), (2), (3), (4)", None, None, ctypes.byref(my_threading_local.err))
lib.sqlite3_exec(my_threading_local.db, "SELECT test(x, 1) FROM a", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb), None, ctypes.byref(my_threading_local.err))
</code>
This program will segfault at the end. The problem is that
