import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_fn.argtypes = (CALLBACK,)
lib.pass_in_fn.restype = ctypes.c_int

# This is the function to pass in.

def fn(arg):
    print("fn", arg)
    return arg * 2

# Call the function

print(lib.pass_in_fn(CALLBACK(fn)))

# This is a function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes
