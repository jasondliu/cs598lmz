import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is a simple C callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is a C function that takes a callback function as an argument
CFUNC = ctypes.CDLL(ctypes.util.find_library('c')).add
CFUNC.argtypes = (ctypes.c_int, ctypes.c_int, CALLBACKFUNC)
CFUNC.restype = ctypes.c_int

# This is a Python callback function
def pyfunc(x, y):
    print 'pyfunc called with %d, %d' % (x, y)
    return x+y

# This is a Python function that takes a callback function as an argument
def pyfunc2(x, y, cb):
    print 'pyfunc2 called with %d, %d' % (x, y)
    return cb(x, y)

# Test the C function with a Python callback function
print 'C function
