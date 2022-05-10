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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_create_disposable_module("test", ctypes.c_void_p(), 0, my_cb)

db = sqlite3.connect(DB_URI, uri=True)

def test_fn(a, b):
    return a

db.create_function("test", 2, test_fn)

my_threading_local.a = db

t = threading.Thread(target=lambda: my_threading_local.a.execute("select test(5, 10)"))

t.start()
t.join()

db.close()

sqlite3.sqlite3_shutdown()
