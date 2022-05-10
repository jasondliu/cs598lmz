import ctypes
# Test ctypes.CFUNCTYPE in the most basic case, with a simple Python
# callback.

import sys
import unittest

import _ctypes_test

class CFunctionTypeTestCase(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        # The argtypes tuple is not required, but should be accepted.
        CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        callback = CALLBACK(self.callback)
        _ctypes_test.set_callback(callback)
        res = _ctypes_test.call_callback(1, 2)
        self.assertEqual(res, 2)
        self.assertEqual(self.got_args, (1, 2))

    def test_errcheck(self):

        def errcheck(result, func, args):
            self.assertEqual(result, 3)
