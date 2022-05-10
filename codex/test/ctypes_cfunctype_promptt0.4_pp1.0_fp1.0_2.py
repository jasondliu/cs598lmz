import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE, which is used to create callbacks.
# This test is not complete, but it should at least make sure that the
# basic functionality works.

import unittest
from ctypes import *

class CFuncPtrTest(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        # The prototype is "int func(int, int)"
        FUNC = CFUNCTYPE(c_int, c_int, c_int)
        func = FUNC(self.callback)

        # Invoke the callback
        result = func(1, 2)
        self.assertEqual(result, 2)
        self.assertEqual(self.got_args, (1, 2))

