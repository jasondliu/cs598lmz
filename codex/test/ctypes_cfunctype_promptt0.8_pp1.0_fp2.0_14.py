import ctypes
# Test ctypes.CFUNCTYPE()
#
# This is the same as for normal functions (_testfunc).
#
# Addresses are (of course) different and we have to pass a class
# instance when called.  The instance is passed as "self" attribute.
#
# The address can be retrieved from the __repr__() of the class
# instance.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]
    def __repr__(self):
        address = ctypes.addressof(self)
        return "<X at %x>" % address

class Y(X):
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        address = ctypes.addressof(self)
        return "<Y at %x>" % address

i = ctypes.c_int
f = ctypes.CFUNCTYPE(i, i)
x = X()
