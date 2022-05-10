import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int callback(int (*func)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg):
    print("func() called with %d" % arg)
    return arg + 1

# Now pass the function to the callback function
res = lib.callback(CALLBACK(func))
print("callback returned", res)

# Now pass a function that takes a different number of arguments
# This should raise a TypeError
def func2(arg, arg2):
    print("func2() called with %d and %d" % (arg, arg2))
    return arg + arg2

try:
    lib.callback(CALLBACK(func2))
except Type
