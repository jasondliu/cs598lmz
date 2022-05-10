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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

class Test(unittest.TestCase):
    def test(self):
        # XXX: This test fails on 32-bit Linux.
        if ctypes.sizeof(ctypes.c_void_p) == 4 and sys.platform == "linux2":
            raise unittest.SkipTest

        # SQLite won't allow multiple connections to an in-memory database.
        # That's why we need this callback.
        sqlite3.sqlite3_initialize()
        sqlite3.sqlite3_auto_extension(my_cb)
        sqlite3.sqlite3_shutdown()

        try:
            a = sqlite3.connect(DB_URI, uri=True)
        finally:
            del a

if __name__ == "__main__":
    unittest.main()
