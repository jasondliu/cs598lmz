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

# Loads the C library
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Creates the SQLite connection
conn = lib.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p(0)))

# Installs the callback
lib.sqlite3_progress_handler(conn, 100, my_cb, 0)

# Creates the table
lib.sqlite3_exec(conn, "CREATE TABLE t(a, b)", None, 0, 0)

# Inserts a row
lib.sqlite3_exec(conn, "INSERT INTO t VALUES (1, 2)", None, 0, 0)

# Selects the row
lib.sqlite3_exec(conn, "SELECT test(a, b) FROM t", None, 0, 0)

# Checks that the callback has been called
assert my_threading_local.a is not None

# Closes the connection
lib.sqlite3_close(conn)
