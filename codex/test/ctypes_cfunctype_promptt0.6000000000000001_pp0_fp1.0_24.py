import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(a, b):
    print(a, b)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

