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
    # load the sqlite driver
    sqlite_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    if not sqlite_lib:
        raise RuntimeError("sqlite3 library not found")

    # register the callback
    sqlite_lib.sqlite3_step_callback(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb), None)

    # create a connection
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c = conn.cursor()

    # create a table
    c.execute("CREATE TABLE test (i int)")

    # insert a row
    c.execute("INSERT INTO test VALUES (1)")

    # select from the table
    c.execute("SELECT test(1, 2) FROM test")

    # fetch the result
    print(c.fetchone()[0])

if __name__ == "__main__":
    main
