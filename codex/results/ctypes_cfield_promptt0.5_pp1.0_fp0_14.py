import ctypes
# Test ctypes.CField
#
# This tests the ctypes.CField class, which is used as a base class
# for ctypes.Field, ctypes.Array and ctypes.Pointer.
#
# It tests the following methods of CField:
# - from_address
# - from_param
# - get
# - set
# - _sizeof
# - _offsetof
#
# It also tests the following methods of Field:
# - _get_offset
# - _get_size

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):

    def test_from_address(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]

        x = X()
        x.a = 1
        x.b = 2

        # Test that from_address returns a pointer to the
        # structure.
        p = ctypes.POINTER(X).from_address(ctypes.addressof(x))
       
