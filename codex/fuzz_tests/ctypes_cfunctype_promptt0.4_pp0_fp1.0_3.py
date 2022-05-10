import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE() factory function.
# It's based on the example in the ctypes documentation.

from ctypes import *

# Define a prototype for the callback functions
CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))

# Define a prototype for the function that takes a callback
FUNCPROTO = CFUNCTYPE(None, CALLBACKFUNC, c_int)

# Define a function that takes a callback and calls it
def func(callback, arg):
    callback(arg, arg, None)

# Convert the Python function to a CFUNCTYPE object
cfunc = FUNCPROTO(func)

# Define a callback function
def mycallback(a, b, c):
    print "mycallback called with", a, b, c
    return 0

# Convert the Python function to a CFUNCTYPE object
cmycallback = CALLBACKFUNC(mycallback)

# Call the function
c
