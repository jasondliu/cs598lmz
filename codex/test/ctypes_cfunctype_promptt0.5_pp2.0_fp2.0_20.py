import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

