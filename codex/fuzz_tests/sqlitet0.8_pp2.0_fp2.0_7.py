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

sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD))
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_shutdown()

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY)")

thread = threading.Thread(target=my_cb, args=(conn,))
thread.start()

thread.join()

my_threading_local.a.execute("INSERT INTO test(id) VALUES (?)", (1,))

# Try to access the threading local conn from this thread
print(conn.execute("SELECT test(1, 2)").fetchone()[0])
