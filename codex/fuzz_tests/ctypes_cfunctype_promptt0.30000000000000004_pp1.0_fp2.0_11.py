import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# test CFUNCTYPE(None)

# This function raises an exception, so we must call it with
# CFUNCTYPE(None)(), so the exception is not printed.
lib.raise_exception.restype = ctypes.CFUNCTYPE(None)
lib.raise_exception()()

# test CFUNCTYPE(c_int)

lib.my_callback.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print('callback called with', arg)
    return arg + 1

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cb = CMPFUNC(callback)

print(lib.my_callback(cb, 3))

# test CFUNCTYPE(c_int, c_int)

lib.my_callback.
