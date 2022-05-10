import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import wintypes

def test_CFUNCTYPE():
    # XXX This test is incomplete.
    # XXX We should test more argument types, and return types.

    # XXX We should also test calling the function with the wrong
    # types.  This should raise a TypeError.

    CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    def callback(a, b):
        print "callback", a, b
        return a + b

    cb = CallbackType(callback)
    assert cb(1, 2) == 3

    # XXX This should raise a TypeError
    # cb(1, 2, 3)

    # XXX This should raise a TypeError
    # cb(1.0, 2.0)

    # XXX This should raise a TypeError
    # cb(1, 2.0)

    # XXX This should raise a TypeError
    # cb(1.0, 2)

    # XXX This should raise
