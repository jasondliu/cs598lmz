import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE() factory creates a type that can be used to
# create function pointers.
#
# The first argument is the return type, the next arguments are
# the argument types.
#
# The function pointer type is callable, and calls the function
# it points to.

# The following function pointer type takes a function pointer
# as first argument, and an integer as second argument.  The
# function it points to returns an integer.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)

# The following function takes a function pointer as first argument,
# and an integer as second argument.  The function it points to
# returns an integer.

def func(callback, arg):
    return callback(arg)

# The following function pointer type takes no arguments, and
# returns an integer.

