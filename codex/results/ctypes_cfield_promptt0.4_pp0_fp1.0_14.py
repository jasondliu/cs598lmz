import ctypes
# Test ctypes.CField.from_address

import unittest
from test import test_support

class CFieldTestCase(unittest.TestCase):

    def test_from_address(self):

        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int)]

        s = C(1, 2, 3, 4)
        self.assertEqual(s.a, 1)
        self.assertEqual(s.b, 2)
        self.assertEqual(s.c, 3)
        self.assertEqual(s.d, 4)

        # This should fail with a ValueError, because the address
        # is not aligned to the size of the field.
        self.assertRaises(ValueError, ctypes.c_int.from_address, id(s) + 1)

        # This should fail with a ValueError, because the address
        # is not aligned to the size
