import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callbackfunc(value):
    print("callbackfunc", value)
    return value + 1

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def cmpfunc(a, b):
    print("cmpfunc", a, b)
    return a - b

# call the function
lib.set_callback(CALLBACKFUNC(callbackfunc))
lib.call_callback(1)

lib.set_cmp(CMPFUNC(cmpfunc))
lib.call_cmp(1, 2)

# call a function with a callback argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.
