import ctypes
# Test ctypes.CField

import unittest

from test import support

class CFoo(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int),
                ('a', ctypes.c_int),
                ('foo', CTypesFoo)]

class Test(unittest.TestCase):
    def test_index(self):
        self.assertEqual(C.b.index, 0)
        self.assertEqual(C.a.index, 1)
        self.assertEqual(C.foo.index, 2)

    def test_ofs(self):
        self.assertEqual(C.b.offset, 0)
        self.assertEqual(C.a.offset, 4)
        self.assertEqual(C.foo.offset, 8)

        self.assertEqual(C.a.offset, C.a.offset)
        self.assertE
