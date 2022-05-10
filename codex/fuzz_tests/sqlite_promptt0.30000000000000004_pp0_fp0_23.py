import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('test.db')
#print "Opened database successfully";
#conn.close()

# Test ctypes.util.find_library()
#print ctypes.util.find_library('c')

# Test ctypes.CDLL()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print libc

# Test ctypes.CDLL().printf()
#libc.printf("Hello, World!\n")

# Test ctypes.CDLL().time()
#print libc.time(None)

# Test ctypes.CDLL().getpid()
#print libc.getpid()

# Test ctypes.CDLL().pthread_create()
#def thread_func(name):
#    libc.printf("Hello from %s!\n", name)
#
#libc.pthread_create.argtypes = [ctypes.c_void_p,
#                                ctypes.c_void_p,
#                                ctypes.c_void
