import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE() factory function.
# It is used to create callback functions.

from ctypes import *
import unittest

class CFUNCTYPETest(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        # Check the CFUNCTYPE() factory function
        # CFUNCTYPE(restype, *argtypes) -> function prototype object

        # The prototype object is callable, and creates real
        # C callable function objects.
        # The callable objects are used to create C callback functions.

        # The prototype object can be called with an error checker
        # function, which is used to check the arguments and return
        # value of the C function.

        # The prototype object can also be called with a string
        # containing the C code for the function.  This is used
        # to create inline callbacks.

        # The prototype object can also be called with a callable

