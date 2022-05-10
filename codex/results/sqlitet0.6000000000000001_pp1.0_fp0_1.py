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
    lib = ctypes.util.find_library("sqlite3")
    sqlite3.sqlite_api_routines.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite_api_routines.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.sqlite_api_routines.sqlite3_config(sqlite3.SQLITE_CONFIG_MEMSTATUS, 0)
    sqlite3.sqlite_api_routines.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

    for i in range(0, 100):
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        a.close()

if __name__ == "__main__":
    main()
    print("Finished")
