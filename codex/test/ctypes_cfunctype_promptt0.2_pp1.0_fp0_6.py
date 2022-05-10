import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function with a callback argument.
# The callback is called with a pointer to an int.
# The callback returns an int.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def func(n):
    print('func', n)
    return n * 2

callback = prototype(func)

# Call the function with the callback.

