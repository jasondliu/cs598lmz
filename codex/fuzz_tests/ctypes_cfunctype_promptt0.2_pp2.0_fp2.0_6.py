import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is derived from the ctypes tutorial, and is used to test
# the ctypes.CFUNCTYPE feature.

from ctypes import *

# Load the library
lib = cdll.LoadLibrary("libc.so.6")

# Declare the prototype of the function
prototype = CFUNCTYPE(c_int, c_int, c_int)

# Create a function that takes two integers and returns an integer
# The function is called "add"
add = prototype(("add", lib), ((1, "i"), (1, "i")))

# Call the function
print add(1, 2)

# Create a function that takes two integers and returns a double
# The function is called "div"
div = prototype(("div", lib), ((1, "i"), (1, "i")))

# Call the function
print div(1, 2)
