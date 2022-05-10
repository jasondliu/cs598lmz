import ctypes
# Test ctypes.CFUNCTYPE
#
# This is the same as the test_cfunctype.py test, except that we use
# ctypes.CFUNCTYPE to create the callback function type.  This is
# important because ctypes.CFUNCTYPE is a Python-level function, and
# the callback function type is a C-level function.
#
# The test_cfunctype.py test is in the same directory as this file,
# and is run by the same test suite.

import unittest
from test import support
from ctypes import *

class CallbackTest(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_simple_callbacks(self):
        self.got_args = None
        cb = CFUNCTYPE(c_int, c_int, c_int)(self.callback)
        restype = c_int
        argtypes = (c_int, c_int)
        #
        # calling the callback directly:
        res = c
