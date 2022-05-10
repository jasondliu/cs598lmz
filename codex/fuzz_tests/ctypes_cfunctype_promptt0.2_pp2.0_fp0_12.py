import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# The following is a simple example of a C callback function.
# It is called from Python, and should return the sum of its
# two arguments.

CALLBACK = CFUNCTYPE(c_int, c_int, c_int)

def py_callback(arg1, arg2):
    print "py_callback called with", arg1, arg2
    return arg1 + arg2

# Now we register the Python function as a callback with ctypes.

cb = CALLBACK(py_callback)

# Now we call a C function, which will in turn call our callback.

libc = CDLL(ctypes.util.find_library("c"))

# The C function is declared as follows:
#
#     int c_callback(int (*callback)(int, int), int arg1, int arg2);

c_callback = libc.c_callback
c_callback.argtypes = [CALLBACK, c_int, c_int]
c_callback.restype = c_int

print c_callback(cb
