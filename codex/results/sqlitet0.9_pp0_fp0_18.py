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

p = ctypes.util.find_library("sqlite3")
p = ctypes.CDLL(p)

#nthread, niter, rc:
#1, 1, 0, 1 (1 memory leaks w/ valgrind)
#1, 10, 0, 1 (1 memory leaks w/ valgrind)
#10, 1, 0, 1 (1 memory leaks w/ valgrind)
#10, 10, 0, ? (none found by valgrind)
nthread = 10
niter = 10

#doesn't matter what rc is, python atexit shouldn't try to free the modified 
#sqlite3 config structure (as in this case)
rc = 1

for i in range(niter):
    threads = []
    for n in range(nthread):
        threads.append(threading.Thread(target=p.sqlite3_config, args=(2, my_cb, rc)))
        threads[-1].start()

    for n in range(nthread):
        threads[n].join()

    for n in range(nthread):

