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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(p))
sqlite3.sqlite3_db_config(p, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, ctypes.byref(rc))
sqlite3.sqlite3_enable_load_extension(p, 1)
sqlite3.sqlite3_load_extension(p, ctypes.util.find_library("sqlite3_extension"), 0, ctypes.byref(err))
sqlite3.sqlite3_close(p)

print(my_threading_local.a.execute("select test(1, 2)").fetchall())
</code>
<code>$ python3 test.py
[(1,)]
</code>

