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
lib.sqlite3_log(lib.SQLITE_CONFIG_LOG, my_cb)

with sqlite3.connect(DB_URI, uri=True) as conn:
    conn.execute("create table a (b)")
    conn.execute("insert into a values (null)")
    conn.execute("select * from a")

del my_threading_local.a
