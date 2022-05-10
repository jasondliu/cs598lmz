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

def another_cb(p):
    assert my_threading_local.a is not None
    my_threading_local.a.close()

sqlite3.sqlite3_enable_shared_cache(0)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SERIALIZED))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_LOG), another_cb, None)

for i in range(1000):
    t = threading.Thread(target=my_cb, args=[])
    t.start()
    t.join()

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG
