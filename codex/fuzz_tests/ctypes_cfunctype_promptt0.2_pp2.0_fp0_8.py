import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function with a callback parameter. The callback
# is called with a pointer to a structure as parameter.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

# The callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.POINTER(X))

def callback(x):
    print(x.contents.a, x.contents.b)

# The function taking the callback
lib.set_callback.argtypes = (CALLBACKFUNC,)

# Call the function
lib.set_callback(CALLBACKFUNC(callback))

# Call the function again, with a different callback
def callback2(x):
    print(x.contents.a * x.contents.b)

lib.set_callback(CALLBACKFUNC(callback2))

# Call
