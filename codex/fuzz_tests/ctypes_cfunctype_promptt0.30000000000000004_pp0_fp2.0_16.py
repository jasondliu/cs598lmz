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
square = prototype((("square", lib), paramflags),
                   (("square", lib), paramflags))

print(square(5))

# This is a function that takes a pointer to a function as an argument.
# The function pointed to is called with one integer argument and its
# return value is returned.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, CALLBACK
