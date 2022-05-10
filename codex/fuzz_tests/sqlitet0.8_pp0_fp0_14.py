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

def my_step(a, b):
    pass

def my_final(x):
    pass

sqlite3.sqlite3_enable_shared_cache(True)

try:
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_collation("DUMMY", my_cb)
    conn.create_aggregate("DUMMY_STEP", 1, my_step, my_final)
    print "nested threading local", my_threading_local.a.execute("SELECT test(1, 2)").fetchone()[0]
except sqlite3.ProgrammingError:
    print "ProgrammingError (expected exception)"

print "shared cache enabled:", sqlite3.sqlite3_enable_shared_cache(True)
print "shared cache enabled:", sqlite3.sqlite3_enable_shared_cache(False)
