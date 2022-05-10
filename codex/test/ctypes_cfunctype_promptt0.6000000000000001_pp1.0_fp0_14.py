import ctypes
# Test ctypes.CFUNCTYPE and class methods

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X:
    def __init__(self):
        self._b = bytes(b'abcd')

    def meth(self, x):
        pass

    @classmethod
    def cmeth(cls, x):
        pass

f = X.meth
cm = X.cmeth

CFUNCTYPE = ctypes.CFUNCTYPE

f_c = CFUNCTYPE(None, ctypes.c_int)(f)
f_c(42)

cm_c = CFUNCTYPE(None, ctypes.c_int)(cm)
cm_c(42)

# calling the C function
