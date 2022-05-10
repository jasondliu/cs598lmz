import ctypes
# Test ctypes.CField()
#
# This test can be run by executing "run_tests --match=ctypes_test --match=test_CField"
#
# If a C compiler is installed, the test will be performed using a
# dynamically loaded shared library.  If no C compiler is installed,
# the test will be performed using the statically linked libtest.so
# library, which is provided in the ctypes source distribution.

#from ctypes import *
from ctypes.test import need_symbol
from ctypes import (CDLL, CFUNCTYPE, Structure, POINTER,
    byref, cast, c_char, c_int, c_void_p)
from ctypes.util import find_library
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        if find_library("m"):
            # If a C compiler is installed, dynamically load a shared
            # library and call a function in that library to set up a
            # Structure, and a function to retrieve the value of a
            # Structure field.
            self.lib = CDLL(
