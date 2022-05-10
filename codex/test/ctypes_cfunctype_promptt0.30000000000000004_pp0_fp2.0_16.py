import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple function that takes an integer argument and returns
# the square of that argument.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

paramflags = (1, "number"),

# The following line is equivalent to:
#
#   square = prototype((("square", lib), paramflags))
#
# except that the name "square" is bound to the function object.
