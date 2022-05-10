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

sqlite3.sqlite3_initialize()

libname = ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(libname)
lib.sqlite3_config(1)

#connections = []
connections = set()

def thread_func():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    connections.add(conn)
    conn.close()
    del conn

threads = []

for i in range(100):
    t = threading.Thread(target=thread_func)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

lib.sqlite3_shutdown()

for conn in connections:
    cur = conn.cursor()
    cur.execute("select test(?)", (2,))
</code>
The output on my machine is as follows:
<code>Exception in thread Thread-12:
Traceback (most recent call last):
 
