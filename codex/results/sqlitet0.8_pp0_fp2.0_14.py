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

so = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
p = ctypes.create_string_buffer(u"CREATE TABLE t1 (id integer primary key)".encode("utf-8"))
so.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db), 2, None)
so.sqlite3_exec(my_threading_local.db.value, p, ctypes.pythonapi.Py_None, None)
p = ctypes.create_string_buffer(u"INSERT INTO t1 VALUES(1)".encode("utf-8"))
so.sqlite3_exec(my_threading_local.db.value, p, ctypes.pythonapi.Py_None, None)
so.sqlite3_autocommit(my_threading_local.db.value, 0)
so.sqlite3_create_function(my_threading_local.db.value, b"func", 1, 2, None,
