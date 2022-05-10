import ctypes
# Test ctypes.CFUNCTYPE

# This test is based on the ctypes tutorial, chapter 5.
# http://starship.python.net/crew/theller/ctypes/tutorial.html

import unittest
from test import test_support

import _ctypes_test

class CFuncPtrTestCase(unittest.TestCase):
    def test_basic(self):
        # some basic tests, first for functions without arguments
        # and return value
        dll = _ctypes_test.dll
        self.failUnlessEqual(dll.my_callback(None), 0)
        self.failUnlessEqual(dll.my_callback(lambda: None), 0)
        self.failUnlessEqual(dll.my_callback(lambda: 42), 42)

        # now for functions with arguments
        self.failUnlessEqual(dll.my_callback(lambda x: x, 42), 42)
        self.failUnlessEqual(dll.my_callback(lambda x, y: x*y, 6, 7), 42)

        # and functions with a return value
        self.failUnlessEqual
