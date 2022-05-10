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

sqlite3.sqlite3_threadsafe()

lib_sqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
lib_sqlite3.enable_shared_cache(0)

lib_sqlite3.sqlite3_config(ctypes.c_int(5), ctypes.c_int(2))

lib_sqlite3.sqlite3_config(ctypes.c_int(7), my_cb)

my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

my_threading_local.a.executescript("create table t(x)")
my_threading_local.a.executescript("insert into t(x) values(1)")

def thread_fn():
    my_threading_local.a.execute("select test(x, ?) from t", (1,))
    my_threading_local.a.execute("select test(x, ?) from t", (
