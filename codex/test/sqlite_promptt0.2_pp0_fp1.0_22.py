import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('test.db')
#print "Opened database successfully";

# Test ctypes.util.find_library()
#print ctypes.util.find_library('c')

# Test ctypes.CDLL()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print libc

# Test ctypes.CDLL.__getattr__()
#print libc.printf

# Test ctypes.CFUNCTYPE()
#CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

# Test ctypes.CFUNCTYPE.__call__()
#cmp_func = CMPFUNC(lambda x, y: 0 if x[0] == y[0] else 1 if x[0] < y[0] else -1)

# Test ctypes.CDLL.__getattr__()()
#array = (ct
