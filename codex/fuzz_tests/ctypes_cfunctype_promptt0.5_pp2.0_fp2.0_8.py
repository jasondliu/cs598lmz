import ctypes
# Test ctypes.CFUNCTYPE() with a simple function that takes a
# single integer argument and returns a single integer.

from ctypes import *

# Create a CFUNCTYPE which takes an integer and returns an integer.
# The first argument is the return type, the rest are the parameter
# types.
int_func = CFUNCTYPE(c_int, c_int)(lambda x: x+1)

# Call the function with an integer.
print int_func(1)

# Call the function with a float.
print int_func(1.0)

# Call the function with a string.
print int_func("1")
