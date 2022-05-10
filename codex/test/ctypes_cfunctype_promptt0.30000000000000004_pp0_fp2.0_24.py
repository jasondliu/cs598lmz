import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test CFUNCTYPE(None)

CALLBACK = ctypes.CFUNCTYPE(None)

def callback():
    print('callback called')

# The callback is called from a C function, it must not raise an
# exception.

CALLBACK_FUNC = ctypes.CFUNCTYPE(None, CALLBACK)

class X(ctypes.Structure):
    _fields_ = [("callback", CALLBACK_FUNC)]

