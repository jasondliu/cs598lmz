import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER(<func-type>)

# The following test was originally written by Thomas Heller:
# http://starship.python.net/crew/theller/ctypes/tutorial.html#pointers-to-functions

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)

# This is the prototype of the function we want to call.
# It takes a function pointer as first argument, and an integer
# as second argument. The function pointer must take an integer
# argument, and return an integer.
#
# The function returns the sum of calling the function pointer
# first with the given integer, and then again with the result
# of the first call.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following creates a function pointer type called 'MyFuncPtrType'
# which takes an integer argument, and returns an integer.

MyFuncPtrType = ctypes.POINTER(prototype)

def add_func(a):
    return a +
