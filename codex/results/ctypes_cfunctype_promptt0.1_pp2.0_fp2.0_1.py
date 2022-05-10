import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function that takes a function pointer as argument
# and calls it.

lib.callit.restype = ctypes.c_int
lib.callit.argtypes = (CALLBACK, ctypes.c_int)

print(lib.callit(CALLBACK(callback), 1))

# This is a function that takes a function pointer as argument
# and calls it.

lib.callit_with_arg.restype = ctypes.c_int
lib.callit_with_arg.arg
