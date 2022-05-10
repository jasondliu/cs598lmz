import ctypes
# Test ctypes.CField.

# The CField class is used by the CStructure class to implement field
# access.

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_field(self):
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        CField = ctypes.CField

        # We need to test that the _offset_ attribute is correctly set,
        # and that alignment is taken into account.
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_char),
                        ("b", ctypes.c_int)]

        self.assertEqual(S.a._offset_, 0)
        self.assertEqual(S.b._offset_, ctypes.sizeof(ctypes.c_int))

        # We need to test that fields can be added dynamically.
        S._fields_.append(("c", ctypes.c_double))
        self.assertEqual(S.c._offset_, c
