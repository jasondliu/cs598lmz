import ctypes
# Test ctypes.CFUNCTYPE(...)(func)

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(arg):
    return arg + 3

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = [CALLBACK]
lib.use_callback.restype = ctypes.c_int

callback = CALLBACK(func)
lib.set_callback(callback)
result = lib.use_callback(5)
print(result)

# Test the "paramflags" parameter
def func(arg1, arg2):
    return arg1 + arg2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = [CALLBACK]
lib.use_callback.restype = ctypes.c_int

callback = CALLBACK(func, paramflags=(1,))
lib.set
