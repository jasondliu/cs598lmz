import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

CALLBACK = Callable(callback)

lib.set_callback(CALLBACK)

res = lib.use_callback(1)
print("use_callback returned", res)

if res != 2:
    raise RuntimeError("callback failed")
