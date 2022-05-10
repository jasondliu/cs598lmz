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

test_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
test_lib.sqlite3_config(2, 1)

sqlite3.enable_shared_cache(True)
sqlite3.register_converter("foo", my_cb)

# get shared connection
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.close()

# create some threads to check that connections can be cached

threads = []

for i in range(50):
    t = threading.Thread(target=my_cb, args=(None,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# check that connections in the threading local is closed

