import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER(ctypes.CFUNCTYPE)

from ctypes import *
import _ctypes_test

def test_CFUNCTYPE():
    # CFUNCTYPE(None) is not allowed
    try:
        CFUNCTYPE(None)
    except TypeError:
        pass
    else:
        raise AssertionError

    # CFUNCTYPE(None, None) is not allowed
    try:
        CFUNCTYPE(None, None)
    except TypeError:
        pass
    else:
        raise AssertionError

    # CFUNCTYPE(None, c_int) is not allowed
    try:
        CFUNCTYPE(None, c_int)
    except TypeError:
        pass
    else:
        raise AssertionError

    # CFUNCTYPE(c_int, None) is not allowed
    try:
        CFUNCTYPE(c_int, None)
    except TypeError:
        pass
    else:
        raise AssertionError

   
