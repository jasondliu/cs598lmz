import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# t = time.time()
# con = sqlite3.connect('data.sqlite')
# print(time.time() - t)


# Test ctypes.util.find_library()
# for lib in ('freetype', 'z', 'c'):
#     print(lib, ctypes.util.find_library(lib))

# Test ctypes.util.find_library()
# print(threading.current_thread().ident)
# thread1 = threading.Thread(target=lambda: print('thread1:', threading.current_thread().ident))
# thread1.start()
# thread1.join()
# print(threading.current_thread().ident)
# thread2 = threading.Thread(target=lambda: print('thread2:', threading.current_thread().ident))
# thread2.start()
# thread2.join()
# print(threading.current_thread().ident)


# Test pyfreetype
from pyfreetype import *
print(version)

font = Font('tests/data/LiberationS
