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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
lib.sqlite3_config(2, 1)
lib.sqlite3_initialize()

con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
con.create_function("noop", 1, lambda *x: None)
my_threading_local.a = con

lib.sqlite3_create_function_v2(con._sqlite_conn, b"test_setup", -1, 1, None, my_cb, None, None, None)

cur = con.cursor()
try:
    cur.execute("create table test(a int); select test_setup();")
except sqlite3.OperationalError:
    pass

cur.execute("INSERT INTO test VALUES (test(1, 2));")
cur.execute("select test(1, 1);")
assert cur.fetchone() == (1,)
