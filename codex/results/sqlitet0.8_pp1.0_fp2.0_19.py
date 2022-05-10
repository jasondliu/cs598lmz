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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.pDB), 0, ctypes.c_void_p())

my_threading_local.pStmt = ctypes.c_void_p()
sqlite3.sqlite3_prepare_v2(my_threading_local.pDB, ctypes.c_char_p(b"select test(?, ?)"), -1, ctypes.byref(my_threading_local.pStmt), 0)

sqlite3.sqlite3_exec(my_threading_local.pDB, ctypes.c_char_p(b"create table test(id int)"), None, None, None)

my_threading_local.fptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
sqlite3.sqlite3_exec(my_threading_local.pDB, ctypes.c_char_p(b"insert into test
