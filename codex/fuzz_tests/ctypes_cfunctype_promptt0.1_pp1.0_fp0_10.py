import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# the callback function
def callback(a, b):
    print("callback", a, b)
    return a + b

# the function taking the callback
lib.call_callback.argtypes = (CALLBACKFUNC, ctypes.c_int)
lib.call_callback.restype = ctypes.c_int

res = lib.call_callback(CALLBACKFUNC(callback), 42)
print("result", res)

# call a function with a callback argument, using a class

class Callback:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        print("callback", self.a, b)
        return self.a +
