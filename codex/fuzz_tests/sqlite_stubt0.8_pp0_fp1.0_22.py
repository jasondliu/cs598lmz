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

def generate_drop_sql_db_conns():
    sqlite3.sqlite3_open_v2(b'', ctypes.byref(my_threading_local.a.dbapi_connection))

ctypes.CDLL(ctypes.util.find_library('sqlite3'), handle=ctypes.c_void_p.in_dll(sqlite3, '_sqlite3_api')).sqlite3_config(readwrite=True, threading_mode=2)
sqlite3.sqlite3_open_v2(b'', ctypes.byref(my_threading_local.a.dbapi_connection))
sqlite3.sqlite3_open_v2(b'', ctypes.byref(my_threading_local.a.dbapi_connection))
sqlite3.sqlite3_open_v2(b'', ctypes.byref(my_threading_local.a.dbapi_connection))
generate_drop_sql_db_conns()
generate_drop_sql_db_conns
