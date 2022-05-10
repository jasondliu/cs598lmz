import ctypes
# Test ctypes.CFields

import unittest
from test import test_support

class TestCFields(unittest.TestCase):
    def test_fields(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_double)]
        self.assertEqual(S._fields_, [("x", ctypes.c_int),
                                      ("y", ctypes.c_double)])
        self.assertEqual(S.x.offset, ctypes.c_int.size)
        self.assertEqual(S.y.offset, ctypes.c_int.size + ctypes.c_double.size)

        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_double),
                        ("z", ctypes.c_int)]
        self.assertEqual(S.x.offset, 0)
        self.assertEqual(S.y.offset, ctypes.
