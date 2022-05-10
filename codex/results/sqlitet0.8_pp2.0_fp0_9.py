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

if __name__ == "__main__":
    import sqlite3

    _init_sqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    _init_sqlite.sqlite3_initialize()

    SQLITE_CONFIG_SINGLETHREAD = 1
    SQLITE_CONFIG_MULTITHREAD = 2

    _init_sqlite.sqlite3_config(SQLITE_CONFIG_MULTITHREAD)

    sqlite3.sqlite3_enable_load_extension(1)
    sqlite3.load_extension("testext", "testext_init")

    a = sqlite3.connect(DB_URI, uri=True)

    for i in range(100):
        a.execute("select test(1,1);")
