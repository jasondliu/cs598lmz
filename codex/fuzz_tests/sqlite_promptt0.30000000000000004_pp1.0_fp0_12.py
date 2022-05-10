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
#print ctypes.util.find_library('m')

# Test ctypes.CDLL()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print libc

# Test ctypes.CDLL().malloc()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print libc.malloc(16)

# Test ctypes.CDLL().malloc() and ctypes.string_at()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#malloc = libc.malloc
#malloc.restype = ctypes.c_void_p
#malloc.argtypes = [ctypes.c_size_t]
#ptr = malloc(16)
#
