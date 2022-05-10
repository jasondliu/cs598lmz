import ctypes
# Test ctypes.CFUNCTYPE with calling the pow(3) function.
import sys
import ctypes

libm = ctypes.CDLL(ctypes.util.find_library("m"))
pow = libm.pow
pow.restype = ctypes.c_double
pow.argtypes = (ctypes.c_double, ctypes.c_double)

CallbackType = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def my_callback(x, y):
    return pow(x, y)

cb = CallbackType(my_callback)
print cb(2, y = 3)

class X(object):
    def __call__(self, x, y):
        return pow(x, y)

cb = CallbackType(X())
print cb(2, y = 3)

print cb(2, 3)

#
# Test ctypes.CFUNCTYPE with unicode names.  This is tricky, because the
# fields in ctypes.Structure
