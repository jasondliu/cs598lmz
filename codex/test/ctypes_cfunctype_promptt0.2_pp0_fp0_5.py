import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the CFUNCTYPE() constructor.

import ctypes
from ctypes import *

#
# First, we test the CFUNCTYPE() constructor.
#

# This is the prototype of the callback functions:
prototype = CFUNCTYPE(c_int, c_int, c_int)

# This is the prototype of the function taking a callback:
def func(callback, a, b):
    return callback(a, b)

# This is the callback function:
