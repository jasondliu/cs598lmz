import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def my_callback(a, b):
    print(a, b)
    return a+b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# test the callback as a function
