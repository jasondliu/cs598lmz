import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int function(int(*)(int))

FUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function takes a function pointer as argument, and calls
# the function with the argument 42.

# The function returns the result of the function call.

# The function is called "pass_function_pointer".

pass_function_pointer = lib.pass_function_pointer
pass_function_pointer.argtypes = (FUNCTYPE,)
pass_function_pointer.restype = ctypes.c_int

# This is the function we pass to the function above.

@FUNCTYPE
def func(arg):
    print("func() called with", arg)
    return arg *
