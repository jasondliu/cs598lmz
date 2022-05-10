import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func', args)
    return args[-1]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This should not crash
