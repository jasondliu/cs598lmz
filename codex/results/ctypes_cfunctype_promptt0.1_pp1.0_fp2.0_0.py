import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking a function pointer as argument
# and calling it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 3

CALLBACKFUNC = ctypes.CFUNCTYPE(None, CALLBACK, ctypes.c_int)

lib.set_callback.argtypes = (CALLBACKFUNC, ctypes.c_int)
lib.set_callback.restype = ctypes.c_int

lib.set_callback(CALLBACKFUNC(callback), 0)

# A function taking a function pointer as argument,
# calling it, and returning the result.

lib.call_callback.argtypes = (CALLBACK, ctypes.c_int)
lib.call_callback.restype = ctypes.c_int

print(lib.call_callback(
