import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

if sizeof(c_int) != sizeof(c_void_p):
    raise Exception("sizeof(c_int) != sizeof(c_void_p)")

# This is the prototype of the callback functions:
prototype = CFUNCTYPE(c_int, c_int, c_int)

# This is the function we want to call from Python:
def callback(a, b):
    print "callback", a, b
    return a + b

# This is the function we want to call from Python:
def callback2(a, b):
    print "callback2", a, b
    return a * b

# Convert the Python function into a C callback function:
c_callback = prototype(callback)
c_callback2 = prototype(callback2)

# This is the function we want to call from C:
@CFUNCTYPE(c_int, c_int, c_int, prototype)
def py_func(a, b, callback):
    print "py_func", a, b
    return
