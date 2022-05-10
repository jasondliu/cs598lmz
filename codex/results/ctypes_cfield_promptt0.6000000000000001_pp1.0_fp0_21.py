import ctypes
# Test ctypes.CField

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_cfield(self):
        # check that ctypes.CFields can be created
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char),
                        ("c", ctypes.c_long)]
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.b.offset, 4)
        self.assertEqual(S.c.offset, 5)

        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char),
                        ("c", ctypes.c_long),
                        ("d", ctypes.c_char * 2)]
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.b.offset, 4)
        self.assertEqual(S
