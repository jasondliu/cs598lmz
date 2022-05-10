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

# CallbackPrototype is a class that can be used to create
# callback functions.  It takes a callable as argument, and
# creates a C callback function from it.

class CallbackPrototype:
    def __init__(self, prototype):
        self.prototype = prototype
        self.functype = ctypes.CFUNCTYPE(prototype)

    def __call__(self, *args):
        return self.functype(self.prototype(*args))

# This is the function that takes a function pointer as argument
# and calls it.

lib.set_callback.argtypes = CALLBACK,
lib.set_callback.restype
