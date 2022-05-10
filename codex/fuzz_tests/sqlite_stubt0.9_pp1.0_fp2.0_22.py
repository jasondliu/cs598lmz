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

start_sqlite_db = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)

my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

start_sqlite_db.sqlite3_open_v2(ctypes.c_char_p(DB_URI.encode("ascii")), ctypes.byref(my_threading_local.db_conn),
    ctypes.c_int(sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE), None)

start_sqlite_db.sqlite3_open_v2.errcheck = lambda result, func, arguments: result

my_db = my_threading_local.db_conn.value

start_sqlite_db.sqlite3_set_autocommit(my_db, 0)

start_sqlite_db.sqlite3_DBconfig(
