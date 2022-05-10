import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# void func(int (*callback)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

