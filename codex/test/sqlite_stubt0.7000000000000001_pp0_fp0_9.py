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

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_config(SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs("test", 500, ctypes.c_int(0), None), 1)

db = sqlite3.connect(DB_URI, uri=True)

db.create_function("test", 1, my_cb)
print("test 1:", db.execute("select test(1)").fetchone()[0])
print("test 2:", db.execute("select test(1)").fetchone()[0])

db.close()
