import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('test.db')
#print "Opened database successfully";

# Test ctypes.util.find_library()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print "libc = %s" % libc

# Test ctypes.CDLL()
#libc = ctypes.CDLL('libc.so.6')
#print "libc = %s" % libc

# Test ctypes.CDLL().malloc()
#libc = ctypes.CDLL('libc.so.6')
#print "libc = %s" % libc
#libc.malloc.restype = ctypes.c_void_p
#libc.malloc.argtypes = [ctypes.c_size_t]
#p = libc.malloc(1)
#print "p = %s" % p

# Test ctypes.CDLL().free()
#libc = ctypes.CDLL('libc.so.6')
#print "
