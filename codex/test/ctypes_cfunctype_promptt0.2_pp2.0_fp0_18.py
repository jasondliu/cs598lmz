import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This one is a function taking a function pointer as argument
# and returning a function pointer.

# The function pointer argument has a simple prototype:
# int foo(int).
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function pointer returned has a more complex prototype:
# void foo(int, char *, double).
CALLBACK2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_double)

# The function pointer returned has a more complex prototype:
# void foo(int, char *, double).
CALLBACK3 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_double)

# The function pointer returned has a more complex prototype:
# void foo(int, char *, double).
CALLBACK
