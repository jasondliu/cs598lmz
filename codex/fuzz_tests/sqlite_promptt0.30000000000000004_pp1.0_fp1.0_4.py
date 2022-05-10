import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('test.db')
#print "Opened database successfully"
#conn.close()

# Test ctypes.util.find_library()
#print ctypes.util.find_library('c')

# Test ctypes.CDLL()
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print libc

# Test ctypes.CDLL.__getattr__()
#print libc.printf

# Test ctypes.CFUNCTYPE()
#CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# Test ctypes.CFUNCTYPE.__call__()
#def py_cmp_func(a, b):
#    print "py_cmp_func", a, b
#    return 0
#cmp_func = CMPFUNC(py_cmp_func)
#print cmp_func

# Test ctypes.c_void_
