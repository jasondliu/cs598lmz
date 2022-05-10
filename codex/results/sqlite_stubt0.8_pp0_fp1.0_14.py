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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.p))
sqlite3.sqlite3_busy_handler(my_threading_local.p, my_cb, None)

def test():
    # test the function
    my_threading_local.a.execute("select test(5, 8)")
    assert my_threading_local.a.fetchone()[0] == 5

"""
# bug:
# If you run this, it will segfault.
# You can run it under valgrind with the following command:
# valgrind -v --leak-check=full --show-reachable=yes --suppressions=~/src/python/sqlite3supp.txt -q --error-exitcode=2 python sqlite3.py
# to get more info


# Note: this is not a full script, just a snippet for a larger program.
# It works fine with the first thread to use it, but after using the second
# thread, it will segfault
