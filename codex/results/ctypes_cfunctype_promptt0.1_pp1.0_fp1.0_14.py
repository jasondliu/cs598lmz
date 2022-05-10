import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# CallbackPrototype is a class that can be used to create
# callback functions.  The instance is the callback function.

CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class CallbackPrototype:
    def __init__(self, func, restype=None, argtypes=()):
        self.func = func
        self.__name__ = func.__name__
        self.argtypes = argtypes
        if restype is not None:
            self.restype = restype

    def __call__(self, *args):
        return self.func(*args)


