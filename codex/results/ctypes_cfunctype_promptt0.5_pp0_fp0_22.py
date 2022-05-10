import ctypes
# Test ctypes.CFUNCTYPE
#
# This test creates a function pointer type, and then creates a
# function pointer of that type and calls it.

# This test is slightly different from test_callbacks.py, because
# the callback function is not a global function.

import sys

from ctypes import *

def callback(x):
    print "callback:", x
    return x*2

callback_type = CFUNCTYPE(c_int, c_int)

class Foo(Structure):
    _fields_ = [
        ("func", callback_type)
        ]

f = Foo()
f.func = callback_type(callback)

print "f.func(42) =", f.func(42)

if sys.platform == "win32":
    import _ctypes_test
    dll = CDLL(_ctypes_test.__file__)

    # Test that the callback can be a method of a C class instance
    class Bar(Structure):
        _fields_ = [
            ("value", c_int)
            ]

    b = Bar()

