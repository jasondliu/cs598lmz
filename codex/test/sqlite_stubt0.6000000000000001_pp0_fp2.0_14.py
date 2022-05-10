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
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.busy_timeout = 1
    conn.execute("CREATE TABLE t (x)")
    conn.execute("INSERT INTO t VALUES (1)")
    conn.execute("INSERT INTO t VALUES (2)")
    conn.execute("INSERT INTO t VALUES (3)")
    conn.execute("INSERT INTO t VALUES (4)")
    conn.execute("INSERT INTO t VALUES (5)")
    conn.execute("INSERT INTO t VALUES (6)")
    conn.execute("INSERT INTO t VALUES (7)")
    conn.execute("INSERT INTO t VALUES (8)")
    conn.execute("INSERT INTO t VALUES (9)")
    conn.execute("INSERT INTO t VALUES (10)")
    conn.commit()
    conn.close()

    ctypes.pythonapi.PyEval_InitThreads()
