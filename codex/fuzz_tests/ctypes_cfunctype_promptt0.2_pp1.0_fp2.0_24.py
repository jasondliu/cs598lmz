import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# the prototype of the callback function is:
# int callback(int arg)
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the prototype of the test function is:
# int test(int arg, callback func)
lib.test.argtypes = (ctypes.c_int, CALLBACKFUNC)

# the callback function
def callback(arg):
    print("callback called with argument", arg)
    return arg + 3

# call the test function
res = lib.test(2, CALLBACKFUNC(callback))
print("test returned", res)
