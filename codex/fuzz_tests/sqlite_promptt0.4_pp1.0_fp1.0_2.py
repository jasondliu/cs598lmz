import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

# Test ctypes
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print libc
# libc.printf("Hello, world!")

# Test threading
def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
