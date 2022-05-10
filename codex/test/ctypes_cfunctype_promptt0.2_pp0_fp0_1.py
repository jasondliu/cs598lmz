import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
# the callback is called with a pointer to a function
# which is called with a pointer to a string

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def callback(s):
    print(s)
    return len(s)

CALLBACK = CALLBACKFUNC(callback)

