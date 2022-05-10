import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int callback(int arg)

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype of the function is:
# int callme(int arg, callbackfunc func)

lib.callme.argtypes = (ctypes.c_int, CALLBACKFUNC)
lib.callme.restype = ctypes.c_int

def callback(arg):
    print("callback called with arg %d" % arg)
    return arg

print(lib.callme(42, CALLBACKFUNC(callback)))

# Test ctypes.PYFUNCTYPE

# The prototype of the function is:
# int pycallback(int arg)

PYCALL
