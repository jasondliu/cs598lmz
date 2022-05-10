import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a callback function
@prototype
def callback(i):
    print("callback", i)
    return i + 1

# call a function that takes a callback
