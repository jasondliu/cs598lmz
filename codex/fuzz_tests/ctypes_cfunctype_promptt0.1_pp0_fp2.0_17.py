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

lib.callit.argtypes = (CALLBACKFUNC,)
lib.callit.restype = ctypes.c_int

print(lib.callit(CALLBACKFUNC(callback)))

# This is a function that takes a function pointer as argument
# and calls it.

lib.callit.argtypes = (CALLBACK,)
lib.callit.restype = ctypes.c_int

print(lib.
