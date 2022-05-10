import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

# The prototype of the function pointer is:
# int func(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the dll.

def func(n):
    print("func() called with", n)
    return n * 2

# Call the dll function, passing func.

lib.pass_func(FUNC(func))

# This is a function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns
# an integer.

# The prototype of the function pointer is:
# int func(void)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int)

# This is the function that will be passed to the
