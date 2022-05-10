import ctypes
# Test ctypes.CFUNCTYPE()
#
# This is a test of the ctypes.CFUNCTYPE() factory function.
#
# ctypes.CFUNCTYPE() is used to define callbacks that can be called from
# C code.
#
# In this test, a generic function is defined which takes a function
# pointer and calls it.  The function pointer is defined using
# ctypes.CFUNCTYPE() to take a single integer argument and return an
# integer.  This is passed to the generic function, which calls the
# function pointer and returns the result to the caller.

# This is the generic function which takes a function pointer and calls
# it.
import ctypes

_lib = ctypes.CDLL(None)

def generic(fn):
    fn.restype = ctypes.c_int
    return _lib._testfunc(fn)

# This is the function type used to define the function pointer.  The
# function takes a single integer and returns an integer.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int
