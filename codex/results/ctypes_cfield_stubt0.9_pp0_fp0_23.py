import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

import unittest

from test.test_descrtut import _test_repr
from test.test_descrtut import _test_unpack


class CFunctionTypeTestCase(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(ctypes.CFuncPtr(ctypes.c_int, ctypes.c_float)(
                                    lambda x: 3.14).restype, ctypes.c_float)
        self.assertEqual(ctypes.CFuncPtr(ctypes.c_int, ctypes.c_float, restype=ctypes.c_double)(
                                    lambda x: 3.14).restype, ctypes.c_double)
        self.assertEqual(ctypes.CFuncPtr(ctypes.c_int, ctypes.c_float, ctypes.c_int, restype=ctypes.c_double)(
                                    lambda x, y: 3.14).argtypes, (ctypes.c_int, ctypes.c_float))

    def test_unpack(
