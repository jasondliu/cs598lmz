import ctypes
# Test ctypes.CFUNCTYPE

# This test is not run automatically.  To run it, execute this file
# directly.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The function takes a pointer to a function as first argument.
# The function takes an integer and returns an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function takes a pointer to a function as first argument.
# The function takes a pointer to a character and returns an integer.

CMPFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_char))

# The function takes a pointer to a function as first argument.
# The function takes a pointer to a character and returns a pointer to a
# character.

CMPFUNC3 = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char))

# The
