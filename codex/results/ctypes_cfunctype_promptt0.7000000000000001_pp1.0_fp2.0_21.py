import ctypes
# Test ctypes.CFUNCTYPE

import sys
import _ctypes_test

import unittest

try:
    set
except NameError:
    from sets import Set as set

class CFuncPtrTestCase(unittest.TestCase):
    def test_basic(self):
        # This function prototype is not supported by ctypes on Windows:
        # CFUNCTYPE(c_int, POINTER(c_int))
        # The ctypes documentation states that the prototype is
        # only supported if the base type is a simple ctypes type.
        # Windows uses a (void *) for the first argument, but the
        # prototype must be (int *).  The problem is that the
        # Microsoft compiler will accept int ** even though it is
        # not ANSI C.
        #
        # Windows also doesn't like "float" as the return type (even
        # though this is ANSI C), so I changed the return type to
        # "double" for Windows.  I didn't change the test data to
        # match, so Windows will return incorrect results.
        if sys.platform == "win32
