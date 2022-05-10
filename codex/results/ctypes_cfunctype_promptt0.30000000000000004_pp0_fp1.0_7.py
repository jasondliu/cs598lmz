import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking a function pointer as argument
# and calling it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, CALLBACK)

lib.pass_a_func.restype = ctypes.c_int
lib.pass_a_func.argtypes = (CALLBACKFUNC, ctypes.c_int)

res = lib.pass_a_func(callback, 1)
print("result", res)

# A function taking a function pointer as argument
# and returning it.
lib.return_a_func.restype = CALLBACKFUNC
lib.return_a_func.argtypes = (ctypes.c_int,)

res =
