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
    # Load sqlite3 library
    sqlite3_lib = ctypes.util.find_library('sqlite3')
    if not sqlite3_lib:
        raise Exception("sqlite3 library not found")
    ctypes.CDLL(sqlite3_lib)

    # Set up sqlite3 callback
    cb_p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, cb_p, None)

    # Connect to the database
    conn = sqlite3.connect(DB_URI, uri=True)

    # Create the test table
    conn.execute("create table test(a, b);")

    # Insert a value into the test table
    conn.execute("insert into test values(1, 2);")

    # Run the test function
    cursor = conn.cursor()
   
