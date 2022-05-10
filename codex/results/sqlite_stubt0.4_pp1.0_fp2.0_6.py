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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db), 0x00000004, None)
sqlite3.sqlite3_exec(my_threading_local.db, "create table test (a, b)", None, None, None)
sqlite3.sqlite3_exec(my_threading_local.db, "insert into test values (1, 2)", None, None, None)

sqlite3.sqlite3_set_authorizer(my_threading_local.db, my_cb, None)

for i in range(1, 100):
    sqlite3.sqlite3_exec(my_threading_local.db, "select test(a, b) from test", None, None, None)

del my_threading_local

# vim: set ft=python sw=4 sts=4 et :
