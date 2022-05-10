import ctypes
# Test ctypes.CFUNCTYPE

# This tests the "CFUNCTYPE" function, which creates C function types.
# The C function types are used to call C functions through ctypes.
# The "CFUNCTYPE" function is used to create callback functions.
#
# For example, if you want a callback function that takes an int and
# returns a int, you can use "CFUNCTYPE" to create a C function type
# that looks like this:
#
#   int callback(int)
#
# You would then pass a Python callable to a C function that takes a
# function pointer as an argument.
#
# The following example is from the Python documentation:
#
#   from ctypes import *
#   prototype = CFUNCTYPE(c_int, POINTER(c_int))
#   def py_divmod(x, y):
#       return (x / y, x % y)
#   c_divmod = prototype(("divmod", dll), ((1,), (1,)))
#   div, mod = c_divmod(5, 3)
#   print
