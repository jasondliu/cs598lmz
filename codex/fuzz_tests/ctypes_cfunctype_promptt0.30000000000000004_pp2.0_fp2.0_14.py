import ctypes
# Test ctypes.CFUNCTYPE

# This is a very simple test of the ctypes.CFUNCTYPE function.  It
# creates a function type, and then creates a function from that type.
# It then calls the function.  The function simply returns the value
# that it was passed.

# The function is created with the CFUNCTYPE function, which takes the
# result type and the argument types.  The result type is ctypes.c_int,
# and the argument type is ctypes.POINTER(ctypes.c_int).

from ctypes import *

# This is the function type that we will be creating
# a function of.
FUNCTYPE = CFUNCTYPE(c_int, POINTER(c_int))

# This is the function that we will be creating.
def py_func(arg):
    return arg[0]

# Create the function.
f = FUNCTYPE(py_func)

# Call the function and print the result.
print f(pointer((c_int)(42)))
