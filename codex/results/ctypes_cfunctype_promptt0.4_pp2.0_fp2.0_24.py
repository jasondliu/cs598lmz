import ctypes
# Test ctypes.CFUNCTYPE()

# This test is for the ctypes module.

# The ctypes module allows to call functions exported from dlls/shared
# libraries and has extensive facilities to create, access and use
# simple and complicated C data types in Python - in full dynamic typing
# style.

# The CFUNCTYPE() function creates a C callable function from a Python
# callable.

# The C callable can be passed to a foreign function exported from a dll.

import unittest
from test import support

from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_simple(self):
        # simple test
        CALLBACK = CFUNCTYPE(c_int, c_int, c_int)
        self.got_args = None

        def func(*args):
            self.assertEqual(args, self.got_args)
            return args[-1]

        cb = CALLBACK(func
