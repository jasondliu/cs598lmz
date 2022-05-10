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

def main():
    sqlite3.sqlite3_shutdown()

    cb_p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)
    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_deserialize(DB_URI, cb_p, None)

    t = threading.Thread(target=my_cb, args=(1,))
    t.start()
    t.join()
    my_cb(1)

    sqlite3.sqlite3_shutdown()

if __name__ == "__main__":
    main()
