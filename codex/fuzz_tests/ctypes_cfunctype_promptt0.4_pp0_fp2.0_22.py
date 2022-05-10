import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_cfunctype.py test in CPython.
#
# The following code is based on CPython's Lib/ctypes/test/test_cfunctype.py.

from __future__ import print_function

import unittest
from test.support import run_unittest

import ctypes
from ctypes import c_int, c_char_p, c_void_p, c_double, c_float

# On some platforms, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) is
# not callable.  This is a bug in ctypes.  The workaround is to
# declare a dummy function first.
def dummy_function(a):
    return a

class CFuncPtrTest(unittest.TestCase):
    def test_call_with_arg(self):
        func = ctypes.CFUNCTYPE(c_int, c_int)(dummy_function)
        self.assertEqual(func(42), 42)

    def test
