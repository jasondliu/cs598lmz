import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

def callback(x, y):
    print("callback", x, y)
    return x + y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.call_function.argtypes = (CALLBACK, ctypes.c_int, ctypes.c_int)
lib.call_function.restype = ctypes.c_int

result = lib.call_function(CALLBACK(callback), 1, 2)
print("result", result)

# call a function with a callback, using a class

class Callback:
    def __init__(self):
        self.counter = 0
    def __call__(self, x, y):
        print("callback", x, y)
        self.counter += 1
        return x + y

cb = Callback()
result = lib.call_
