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
