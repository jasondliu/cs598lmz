import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the ctypes tutorial:
# http://starship.python.net/crew/theller/ctypes/tutorial.html
#
# The tutorial is in the public domain.

import unittest
from test import test_support

import ctypes

class CFuncPtrTestCase(unittest.TestCase):

    def test_CFuncPtr(self):
        # A simple example of using ctypes to wrap a C function
        #
        # The C function to be wrapped is:
        #
        #     int add(int a, int b) {
        #         return a+b;
        #     }
        #
        # The wrapper is:
        #
        #     int add(int a, int b) {
        #         int c;
        #         c = add.argtypes[0](a, b);
        #         return c;
        #     }
        #
        # The wrapper is compiled and loaded into the process address space
        # using ctypes.CDLL.  The wrapper is then called using the
        #
