import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *

# This is the prototype of the callback function
# The first argument is the return type, the rest are
# the argument types.
#
# The prototype is followed by the name of the callback
# function.
#
# The prototype is used to create a C function pointer
# type, which is then used to create a callback function
# object.

prototype = CFUNCTYPE(c_int, c_int, c_int)

