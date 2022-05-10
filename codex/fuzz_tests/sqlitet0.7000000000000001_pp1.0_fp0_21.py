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

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SINGLETHREAD), 1)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD), 0)

sqlite3.sqlite3_open(b"test", ctypes.byref(my_threading_local.a))

sqlite3.sqlite3_prepare_v2(my_threading_local.a, b"select test(1, 2)", -1, ctypes.byref(my_threading_local.stmt), 0)

sqlite3.sqlite3_exec(my_threading_local.a, b"create table test (id int)", 0, 0, 0)

sqlite3.sqlite3_step(my_threading_local.stmt)

sqlite3.sql
