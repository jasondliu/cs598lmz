import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.FUNCFLAG_USE_ERRNO, ctypes.Py_ssize_t.
#
# This test is run by buildbot, do not add any dependencies which have
# not been released yet.

from ctypes import *
import unittest
from test import support

def callback(*args):
    return len(args)

class FuncTestCase(unittest.TestCase):

    def test_func(self):
        Py_ssize_t = c_ssize_t

        @CFUNCTYPE(c_int, c_int)
        def func(n):
            return n + 1

        self.assertEqual(func(3), 4)

        # this call uses Py_ssize_t, which is a typedef for either
        # int or long, depending on the platform
        @CFUNCTYPE(Py_ssize_t, c_int)
        def func2(n):
            return n + 1

        self.assertEqual(func2(3), 4)

        self.assertRaises(OverflowError
