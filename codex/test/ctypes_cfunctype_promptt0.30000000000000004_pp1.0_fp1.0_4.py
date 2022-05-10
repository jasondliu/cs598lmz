import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    return args

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFuncPtr(func)
