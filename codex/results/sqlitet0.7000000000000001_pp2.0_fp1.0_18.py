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

class Thread(threading.Thread):
    def __del__(self):
        self.join()

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
sqlite3.sqlite3_initialize()
sqlite3.create_function("test", 2, test_fn)
sqlite3.sqlite3_enable_shared_cache(0)

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.pthread_atfork(None, None, my_cb)

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("CREATE TABLE test(a)")
conn.execute("INSERT INTO test VALUES (1), (2)")

for i in range(10):
    t = Thread(target=conn.execute, args=("SELECT test(a, ?) FROM test", (i,)))
    t.start()
    del t
</code>
When I
