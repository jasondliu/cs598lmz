import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_callbacks test.
#
# This test is intended to be run from the Python build directory with:
# ./python Lib/test/regrtest.py test_ctypes_callbacks
#
# It is expected to fail with a segfault when run with the system Python.

import unittest
from test import support
from ctypes import *

class CallbacksTestCase(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def check_type(self, typ, arg):
        self.got_args = None
        cb = CFUNCTYPE(typ, *[typ] * len(arg))(self.callback)
        res = cb(*arg)
        self.assertEqual(res, arg[-1])
        self.assertEqual(self.got_args, arg)

    def test_byte(self):
        self.check_type(c_byte, (1, -
