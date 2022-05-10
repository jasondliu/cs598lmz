import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called.

@CMPFUNC
def func(i):
    print('func', i)
    return i * 2

# Call the function in the dll.  The integer it returns is the
# address of the function pointer it was passed.

