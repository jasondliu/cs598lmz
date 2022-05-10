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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(3, my_cb, None)

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

with db:
    db.execute("create table test(a, b)")
    db.execute("insert into test(a, b) values (?, ?)", (1, 2))
    db.execute("select * from test")
    print(db.execute("select test(a, b) from test").fetchone())
    print(my_threading_local.a.execute("select test(a, b) from test").fetchone())
    print(my_threading_local.a.execute("select count(*) from test").fetchone())
