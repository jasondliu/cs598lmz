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

# Create the threads
threads = []
for i in range(0, 1):
    t = threading.Thread(target=my_cb, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

sqlite3.sqlite3_shutdown()

# Load the extension
extension = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

# Find the function in the extension
create_function = extension.sqlite3_create_function_v2

# Define the argtypes
