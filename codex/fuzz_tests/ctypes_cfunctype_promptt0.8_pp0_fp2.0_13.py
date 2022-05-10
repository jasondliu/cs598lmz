import ctypes
# Test ctypes.CFUNCTYPE
#

import sys
import unittest
from test import test_support
from ctypes import *

##
# Check that new style classes implement the __ctypes_from_outparam__
# method, and that derived classes override the method of the base
# class.

class X(Structure):
    _fields_ = [("a", c_int)]

class XS(X):
    _fields_ = [("b", c_int),
                ("c", c_int)]

class XX(X):
    _fields_ = [("d", c_int),
                ("e", c_int)]

class XXS(XS, XX):
    _fields_ = [("f", c_int),
                ("g", c_int)]

class Test(unittest.TestCase):

    def test_ctypes_from_outparam(self):

        def check(C):

            def check_derived(D):
                self.assertNotEqual(D, C)

                def _(*args):
                    return None

                self.assertEqual(
