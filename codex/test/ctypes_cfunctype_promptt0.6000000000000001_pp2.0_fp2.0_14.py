import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test of the ctypes.CFUNCTYPE function, which creates a
# ctypes callback function prototype.
#
# This test is based on the test of the same name in the Python test
# suite, test_ctypes.

# This test is not meant to be run directly.  It should be run from the
# test_ctypes.py test file.

from ctypes import *
import unittest

class CFuncPtrTestCase(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def check_type(self, typ, argtypes):
        cb = CFUNCTYPE(typ, *argtypes)(self.callback)
        res = cb(*range(len(argtypes)))
        self.failUnlessEqual(self.got_args, tuple(range(len(argtypes))))
        self.failUnlessEqual(res, len(argtypes)-1)

