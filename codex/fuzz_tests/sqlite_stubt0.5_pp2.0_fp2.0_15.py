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

sqlite3.sqlite3_enable_shared_cache(True)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_shutdown()
lib.sqlite3_config(1, my_cb, None)
lib.sqlite3_initialize()

conn = sqlite3.connect(DB_URI, uri=True)

def thread_fn():
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("select test(1, 2)")

threads = []
for i in range(1000):
    t = threading.Thread(target=thread_fn)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

conn.execute("select test(1, 2)")

print("ok")
