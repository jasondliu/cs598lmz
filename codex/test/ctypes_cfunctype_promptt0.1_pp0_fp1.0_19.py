import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# CallbackPrototype is a class that has the same signature as the
# callback function.  It is used to check that the callback
# function has the correct signature.
class CallbackPrototype(object):
    def __init__(self, prototype, paramflags):
        self.prototype = prototype
        self.paramflags = paramflags

# This is the function that will be called by the C code
def py_callback(arg):
    print("py_callback called with", arg)
    return arg + 1

# This is the function that will be called by the C code
