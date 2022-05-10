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

def test(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a


p = ctypes.create_string_buffer(b"hello")
q = ctypes.create_string_buffer(b"hello")

r = ctypes.create_string_buffer(b"hello")

# The Python threading module uses the ctypes module, so using the
# ctypes module directly while using Python threads may produce
# unexpected results.

# This is not the case here, but if you're using Python threads, you'll
# need to either wait for the threads to exit, or use the threading
# module instead.
double_free = False

async def main(loop):
    # Initialize the sqlite library.
    sqlite3.sqlite3_initialize()

    # Creating an SQLite threading mode structure
    sql
