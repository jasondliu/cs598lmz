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

def py_callback(arg1, arg2):
    print "Callback called with arguments", arg1, arg2
    return arg1 + arg2

# create a C function pointer type
c_callback = prototype(py_callback)

# create a callback function object
callback = c_callback

# call the callback function
res = callback(1, 2)
print "Result of callback is", res

# The callback function object can be passed to a C function
# which takes a function pointer as an argument.

# This is the prototype of the C function
# The first argument is the return type, the rest are
# the
