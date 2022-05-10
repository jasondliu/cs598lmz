import ctypes
# Test ctypes.CField type
# This tests all operations on ctypes.CField

import unittest, sys
from test import test_support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ulong),
                ("b", ctypes.c_int * 4),
                ("c", ctypes.c_wchar * 3),
                ("d", ctypes.c_char * 4),
                ]
if sys.platform == 'darwin':
    # OS X
    X._pack_ = 2

class TestCField(unittest.TestCase):

    def test_setattr(self):
        x = X()
        x.a = 1234
        self.assertEqual(x.a, 1234)
        x.b[0] = 42
        self.assertEqual(x.b[0], 42)
        x.c[1] = u'\u1234'
        self.assertEqual(x.c[1], u'\u1234')
        x.d[2] = 'x'
       
