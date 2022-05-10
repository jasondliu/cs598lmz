import ctypes
# Test ctypes.CFUNCTYPE() function
#
# $Id: test_cfunt.py 65311 2008-05-13 09:22:42Z georg.brandl $

import unittest
from test.test_support import run_unittest
from ctypes import (CFUNCTYPE, py_object,
                    c_int, c_char_p, c_void_p, c_double, c_long, c_size_t)

class CFuncTestCase(unittest.TestCase):

    def test_call_c_function(self):
        from ctypes import cdll, c_int
        dll = cdll.msvcrt
        func = CFUNCTYPE(c_int, c_int, c_int)(("atoi", dll), ((1, "x"), (1, "y")))
        self.assertEqual(func(b"42"), 42)

    def test_call_c_function_unicode(self):
        from ctypes import cdll, c_int
        dll = cdll.msvcrt
        func
