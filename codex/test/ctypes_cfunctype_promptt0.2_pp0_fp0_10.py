import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype a function with a callback argument
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a callback function
def mycallback(i):
    print("mycallback", i)
    return i + 1

# call the function
