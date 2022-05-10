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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MEMSTATUS, 0)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

def my_thread():
    for i in range(100):
        x = my_threading_local.a.execute("SELECT test(1, 2)")

threads = [threading.Thread(target=my_thread) for i in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(
