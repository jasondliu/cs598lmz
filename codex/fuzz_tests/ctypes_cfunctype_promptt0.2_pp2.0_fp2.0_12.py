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

# This is the function that we pass to the dll.
# It adds 42 to the argument, and returns the result.
@FUNC
def func(i):
    return i + 42

# Call the dll function. The dll function calls our func() function
# and returns the result.
res = lib.use_int_param(func)
print(res)

# This is a function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns
# an integer.

# The prototype of the function pointer is:
# int func(void)
FUNC = ctypes.CFUNCTYPE
