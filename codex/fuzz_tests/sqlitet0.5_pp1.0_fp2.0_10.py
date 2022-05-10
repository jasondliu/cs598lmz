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
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_shared_cache(1)

threads = []

for i in range(10):
    t = threading.Thread(target=my_cb, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

a = my_threading_local.a

a.execute("create table test (a, b)")
a.execute("insert into test values (1, 'test')")
a.execute("insert into test values (2, 'test2')")
a.execute("select test(a, b) from test").fetchall()
a.execute("select test(a, b) from test").fetchall()
a.execute("
