import ctypes
# Test ctypes.CFUNCTYPE
# This is a test of the ctypes.CFUNCTYPE function.
# It tests that the CFUNCTYPE function can be used to create callable
# objects.
#
# It also tests that the callable object can be called with the correct
# number of arguments, and that the callable object returns the correct
# value.

from ctypes import *

# The function prototype for the function we will call.
# This is the same as the function prototype for the C function
# we will call.

prototype = CFUNCTYPE(c_int, c_int, c_int)

# The function to call.

def py_add(a, b):
    return a + b

# The function to call.

def py_sub(a, b):
    return a - b

# The function to call.

def py_mul(a, b):
    return a * b

# The function to call.

def py_div(a, b):
    return a / b

# The function to call.

