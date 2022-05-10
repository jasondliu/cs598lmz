import ctypes
# Test ctypes.CField
import unittest
from ctypes import *

# Example class
# this is not a complete description of FILE, but it's good
# enough to provide an example.  See also _ctypes_test.c

# See http://msdn.microsoft.com/en-us/library/t1zz5y8c(VS.80).aspx


class FILE(Structure):
    _fields_ = [("_ptr", c_char_p),
                ("_cnt", c_int),
                ("_base", c_char_p),
                ("_flag", c_int),
                ("_file", c_int),
                ("_charbuf", c_int),
                ("_bufsiz", c_int),
                ("_tmpfname", c_char_p)]

import _testcapi

class TestCase(unittest.TestCase):

    def test_simple_type(self):
        self.assertEqual(c_int.in_dll(_testcapi, "simple_type").value, 3)

    def test_intarray(self):
