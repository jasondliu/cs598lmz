import ctypes
# Test ctypes.CFUNCTYPE() by passing a callback which takes a callback and
# calls it immediately.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(cb):
    cb(42)

# cb pointer
CBTy1 = ctypes.CFUNCTYPE(None, ctypes.c_int)
CALLCB = CBTy1(func)

