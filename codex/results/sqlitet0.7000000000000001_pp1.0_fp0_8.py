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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_db_config(my_cb(None), sqlite3.SQLITE_DBCONFIG_LOOKASIDE, 1, 1)

prefix = ctypes.util.find_library("sqlite3")
if prefix:
    sqlite3.load_dll(prefix=prefix, reset_internal_state=True)

def do_test():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

threads = []

for i in range(10):
    t = threading.Thread(target=do_test)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
