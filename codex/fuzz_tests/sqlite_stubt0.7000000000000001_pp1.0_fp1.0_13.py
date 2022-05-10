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

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(my_threading_local.conn), 3 | 0x00000040, None)

sqlite3.sqlite3_prepare_v2(my_threading_local.conn, "select test(1, 2);", -1, ctypes.pointer(my_threading_local.stmt), None)

sqlite3.sqlite3_exec(my_threading_local.conn, "create table test(a);", None, None, None)

sqlite3.sqlite3_create_function(my_threading_local.conn, "test", 2, 1, my_threading_local.a, my_cb, None, None)

sqlite3.sqlite3_step(my_threading_local.stmt)

sqlite3.sqlite3_finalize(my_threading_local.stmt)

sqlite3.sqlite3_close_v2(my_threading_
