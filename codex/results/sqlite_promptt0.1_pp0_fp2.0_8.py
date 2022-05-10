import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

# Test ctypes.util.find_library
# print ctypes.util.find_library('c')

# Test threading.Thread
# def worker():
#     print 'Worker'
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# Test ctypes.CDLL
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print libc.time(None)

# Test ctypes.CDLL(None)
# libc = ctypes.CDLL(None)
# print libc.time(None)

# Test ctypes.CDLL('libc.so.6')
# libc = ctypes.CDLL('libc.so.6')
# print
