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

my_cb_p = sqlite3.SQLiteError(1)
my_cb_p.__del__ = lambda: my_cb(my_cb_p)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_shared_cache(1)
lib.sqlite3_config(sqlite3._sqlite.SQLITE_CONFIG_LOG, my_cb_p, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cursor = a.cursor()
cursor.execute("select test(1, 2)")
cursor.fetchone()
cursor.execute("select test(1, 2)")
cursor.fetchone()
a.close()
del a

b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cursor = b.cursor()
cursor.execute("select test(1, 2)")
cursor.fetch
