import ctypes
# Test ctypes.CFUNCTYPE for multiple return values

from ctypes import *
import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_restype_argtypes(self):
        # ctypes.CFUNCTYPE(restype, *argtypes)
        #
        # restype and argtypes may be None, or a type object or a tuple
        # containing type objects.
        #
        # If restype is None, the restype of the function is int.
        #
        # If no argtypes are given, the argtypes of the function are
        # (c_int, c_int).
        #
        # If argtypes is None, no argtypes are set.
        #
        # If argtypes is a type object, the function takes one argument
        # of this type.
        #
        # If argtypes is a tuple, the function takes arguments of the
        # types contained in the tuple.
        #
        # The function is created and then called.  The return value is
        # checked against a list of expected values.
       
