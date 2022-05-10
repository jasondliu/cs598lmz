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

sqlite3.sqlite_initialize()

sqlite3.enable_shared_cache(False)
sqlite3.sqlite_set_authorizer(my_cb, my_threading_local)

# set up DB
db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.execute("create table test(a, b)")
db.execute("insert into test (a, b) values (1, 2)")

def leak():
    # open db and create function
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.row_factory = sqlite3.Row
    conn.create_function("test", 2, lambda a, b:a)

    c = conn.cursor()
    c.execute("select test(a, b) from test")

    res = c.fetchone()[0]
 
    del c

