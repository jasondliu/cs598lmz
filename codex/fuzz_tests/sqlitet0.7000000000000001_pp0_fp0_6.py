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

def my_close(p):
    del my_threading_local.a

sqlite3.sqlite3_enable_load_extension(True)

sqlite3.sqlite3_auto_extension(
    sqlite3.create_function(
        "my_cb",
        0,
        my_cb
    )
)

sqlite3.sqlite3_auto_extension(
    sqlite3.create_function(
        "my_close",
        0,
        my_close
    )
)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.enable_load_extension(True)
a.load_extension("my_cb")

print (my_threading_local.a.execute("select test(?,?)", [1,2]).fetchone())

a.load_extension("my_close")

print ("done")
