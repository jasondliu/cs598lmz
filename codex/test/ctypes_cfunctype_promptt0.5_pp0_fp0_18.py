import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func', args)
    return args[-1]

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFuncPtr(func)

assert cfunc(1, 2) == 2
