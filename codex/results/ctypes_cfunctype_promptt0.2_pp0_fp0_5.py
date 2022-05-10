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
def callback(a, b):
    print "callback(%d, %d) called" % (a, b)
    return a + b

# Convert the Python callback function into a C callback function.
CMPFUNC = prototype(callback)

# Call the C function using the C callback.
print func(CMPFUNC, 1, 2)

#
# Now, we test the CFUNCTYPE() constructor with a function pointer.
#

# This is the prototype of the callback functions:
prototype = CFUNCTYPE(c_int, c
