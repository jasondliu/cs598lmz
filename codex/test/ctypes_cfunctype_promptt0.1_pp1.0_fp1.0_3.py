import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

def func(*args):
    print(args)
    return args[0]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

