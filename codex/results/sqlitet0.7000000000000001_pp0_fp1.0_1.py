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

# This is going to trigger the bug.
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

# Test loading this under different conditions.
for x in range(2):
    # Test with a thread and without a thread.
    if x == 1:
        t = threading.Thread(target=lambda: None)
        t.start()
        t.join()
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)
    sqlite3.sqlite3_open_v2(DB_URI, 0, None)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.sqlite3_open_v2(DB_URI, 0, None)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)

# Now, wait for something to trigger the bug.
while True:
    pass
