import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This is the prototype of the function we want to call.
# It is a simple function that takes an integer and returns
# the square of this integer.

# This is the prototype of the function we want to call.
# It is a simple function that takes an integer and returns
# the square of this integer.

# The actual function is called 'square' in the _ctypes_test
# module.

# The actual function is called 'square' in the _ctypes_test
# module.

PROTOTYPE = CFUNCTYPE(c_int, c_int)

# The rest is simple.  We get the function from the dll,
# assign it to a python variable, and call it.

# The rest is simple.  We get the function from the dll,
# assign it to a python variable, and call it.

square = lib.square
square.argtypes = (c_int,)
square.restype = c_int

print(
