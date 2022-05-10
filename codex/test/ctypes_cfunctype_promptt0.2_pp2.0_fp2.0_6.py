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
