import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking a function pointer as argument.
# The function pointer takes an int argument and returns an int.

# This is the function pointer type.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function taking a function pointer as argument.
# The argtypes list is required, otherwise the call fails with
# TypeError: wrong type
lib.pass_in_fn_ptr.argtypes = (CALLBACK,)

# This is the function to be passed as function pointer.
def fn(arg):
    print("fn() called with %d" % arg)
    return arg + 1

# This is the function to be passed as function pointer.
# It returns a pointer to a function.
def fn2(arg):
    print("fn2() called with %d" % arg)
    return fn

# This is the function to be passed as function pointer.
# It returns a pointer
