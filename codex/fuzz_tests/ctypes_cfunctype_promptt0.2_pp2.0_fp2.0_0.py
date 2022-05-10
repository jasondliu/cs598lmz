import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument and return
# an integer.

CALLBACKFUNC = CFUNCTYPE(c_int, c_int)

def callback(n):
    print("callback called with", n)
    return n + 1

# This is the function we want to call.  It takes a function pointer
# as first argument, and an integer as second argument.  It calls
# the function pointed to with the integer argument, and returns
# the result of the function.

lib.pass_in_a_callback.argtypes = CALLBACKFUNC, c_int
lib.pass_in_a_callback.restype = c_int

res = lib.pass_in_a_callback(CALLBACKFUNC(callback), 1)
print("result:", res)

# This is the same, but we pass the function pointer as keyword
# argument.

lib.pass_
