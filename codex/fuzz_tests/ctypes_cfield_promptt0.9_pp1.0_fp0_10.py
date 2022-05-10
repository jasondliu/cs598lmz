import ctypes
# Test ctypes.CField.from_address,
# partially from http://bugs.python.org/issue8319
#
# The struct module's from_address function is tricky,
# because it needs to be prepared; it seems to have some rules
# about whether the buffer is writable.
from ctypes import *
from support import unlink
import sys
from ctypes.test import need_symbol

test_dll = CDLL(need_symbol('testdll.dll'))

try:
    c_int_p = POINTER(c_int)
    c_float_p = POINTER(c_float)
    c_long_p = POINTER(c_long)
except TypeError:
    raise unittest.SkipTest("no POINTER type")

class StructTestCase(unittest.TestCase):

    def setUp(self):
        self.s = Struct("4i4f")
        self.p = POINTER(self.s)

    def check_Struct(self, s):
        self.assertEqual(sizeof(s), self.s.size)
        self
