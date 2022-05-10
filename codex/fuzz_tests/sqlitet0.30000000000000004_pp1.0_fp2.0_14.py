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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, None)
    sqlite3.set_progress_handler(my_cb2, None)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("CREATE TABLE test(a, b)")
    conn.execute("INSERT INTO test VALUES (1, 2)")
    conn.execute("SELECT test(a, b) FROM test")
    conn.close()

if __name__ == "__main__":
    main()
