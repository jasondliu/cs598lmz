import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not exhaustive, but should be enough to catch common errors.
#
# The 'self' argument is a hack to make this test work with the unittest
# framework.  The test case is actually created in the setUp() method.

from ctypes import *
import unittest

class CFuncPtrTestCase(unittest.TestCase):

    def setUp(self):
        self.functype = CFUNCTYPE(c_int, c_int, c_int)
        self.func = self.functype(self.myfunc)

    def myfunc(self, a, b):
        return a + b

    def test_argtypes(self):
        self.assertEqual(self.func.argtypes, (c_int, c_int))

    def test_restype(self):
        self.assertEqual(self.func.restype, c_int)

    def test_call(self):
        self.assertEqual(self.func(1, 2), 3)

