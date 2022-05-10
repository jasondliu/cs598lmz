import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#
# This is the equivalent of:
#
#     int (*)(int)
#
# in C.
#
# The returned function pointer should be callable with an integer argument.
#
# The function pointer should be able to be passed to another C function.
#
# The function pointer should be able to be stored in a ctypes instance
# attribute.

import unittest
from test import support

import _ctypes_test

lib = _ctypes_test.dll

class CFuncPtrTestCase(unittest.TestCase):
    def test_call(self):
        f = lib.my_function
        self.assertEqual(f(42), 42)

    def test_call_from_other_dll(self):
        f = lib.my_function
        self.assertEqual(lib.call_my_function(f, 42), 42)

    def test_store_in_instance(self):
        class X(ctypes.Structure):
            _fields_ = [("
