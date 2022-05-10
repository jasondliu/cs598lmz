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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
lib.sqlite3_initialize()

db = sqlite3.connect(DB_URI, uri=True)
db.execute("create table test(a, b)")
db.execute("insert into test(a, b) values (1, 2)")
db.execute("insert into test(a, b) values (3, 4)")
db.execute("insert into test(a, b) values (5, 6)")

lib.sqlite3_stmt_status(None, 1, ctypes.c_int(1), ctypes.c_int(0))
lib.sqlite3_stmt_status(None, 1, ctypes.c_int(1), ctypes.c_int(1))

db.create
