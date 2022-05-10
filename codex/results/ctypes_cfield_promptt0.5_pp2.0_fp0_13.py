import ctypes
# Test ctypes.CField.

import ctypes
import unittest

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_char),
        ("b", ctypes.CField)
    ]

class CFieldTest(unittest.TestCase):
    def test_CField(self):
        self.assertEqual(ctypes.sizeof(X), 4)

if __name__ == "__main__":
    unittest.main()
