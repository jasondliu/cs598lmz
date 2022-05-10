import ctypes
# Test ctypes.CField
#
# On 32-bit x86, a long double takes 10 bytes, of which the 10'th is
# unused.  The alignment of a long double is 8 bytes.  On 64-bit x86 it
# takes 16 bytes, using all 16.
#
# On PowerPC, long double takes 16 bytes, using all 16.  The alignment
# of a long double is 16 bytes.

import unittest
from ctypes import *

class CFieldTest(unittest.TestCase):
    def test_00(self):
        addr = create_string_buffer(1000)
        p = POINTER(c_int)

        class X(Structure):
            _fields_ = [("a", c_char),
                        ("b", c_longdouble)]

            _pack_ = 4

            def __init__(self):
                self.b = 3.14

            def __getitem__(self, i):
                return self.b[i]


        class Y(Structure):
            _fields_ = [("a", c_char),
                        ("b", c_long
