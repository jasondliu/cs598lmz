import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

#
# First test the basic ctypes.CFUNCTYPE function.
#

# This function is called with a function pointer as first argument,
# and an integer as second argument.  The function pointer is called
# with the integer as argument, and should return the integer.

CALLBACK = CFUNCTYPE(c_int, c_int)

@CALLBACK
def func(arg):
    return arg

result = lib.pass_through(func, 42)
if result != 42:
    raise Exception("%d != 42" % result)

#
# Now test the error handling.
#

# This function is called with a function pointer as first argument,
# and an integer as second argument.  The function pointer is called
# with the integer as argument, and should return the integer.

CALLBACK = CFUNCTYPE(c_int, c_int)

@CALLBACK
def func(arg):
    return arg

# The
