import ctypes
# Test ctypes.CField(foobar)
import ctypes.util
import ctypes._endian as _endian # This is most easily tested indirectly ...

import unittest
from test.support import run_unittest
from test import string_tests

libm = ctypes.CDLL(ctypes.util.find_library("m"))
h = ctypes.c_short(42).value
H = ctypes.c_ushort(42).value
i = ctypes.c_int(42).value
I = ctypes.c_uint(42).value
l = ctypes.c_long(42).value
L = ctypes.c_ulong(42).value

class TestMisc(unittest.TestCase):

    def test_0(self):
        # test _as_parameter_
        self.assertEqual(ctypes.c_int(42)._as_parameter_, 42)

    def test_1(self):
        # tests from_param
        self.assertEqual(ctypes.c_long.from_param(42), 42)
        self
