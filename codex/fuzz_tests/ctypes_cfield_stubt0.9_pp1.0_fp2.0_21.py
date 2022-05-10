import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class C2Field(ctypes.CField):
    "For testing against swig.cdata"
    _type_ = str
    _cast = staticmethod(str)

test_src = """\
from ctypes import *
import unittest

class CFieldTests(unittest.TestCase):
    def test_x(self):
        self.assertEqual(S.x._type_, c_int)

        s = S()
        self.assertEqual(s.x, 0)
        self.assertEqual(type(s.x), c_int)
        self.assertEqual(type(S.x), CField)

        s.x = 42
        self.assertEqual(s.x, 42)
        self.assertEqual(S.x.__get__(s), 42)

        s.x = "foo"
        self.assertEqual(s.x, 0)
        self.assertEqual(S.x.__set__(s, "foo"), None)
        self.assertEqual(s.
