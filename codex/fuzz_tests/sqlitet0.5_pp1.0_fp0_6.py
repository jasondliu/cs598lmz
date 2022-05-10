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
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, None)
    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

main()

# The following is not thread-safe, but should be ok for this test case,
# since the test case is single-threaded.
libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

if libc.malloc_stats() == -1:
    # We're on a system that doesn't support malloc_stats()
    pass
else:
    # We're on a system that does support malloc_stats().  Check that the
    # connection is closed.
    malloc_stats_before = libc.malloc_stats()
    my_threading_local.a = None
    malloc_stats_after = libc.malloc_stats()
    if malloc_stats_before != malloc_stats_after:

