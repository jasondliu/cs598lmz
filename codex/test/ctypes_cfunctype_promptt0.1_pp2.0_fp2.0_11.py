import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an int argument, and return an int.

# The prototype of the function pointer is:
# int func(int)
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that takes a function pointer as argument.
# The function pointer is passed as keyword parameter 'func'.
# The function returns the result of calling the function pointer.
# The function pointer is called with 42 as argument.

# The prototype of the function is:
# int callit(int (*func)(int), int arg)
