import ctypes
# Test ctypes.CFUNCTYPE, callbacks and the error handler
#
# by Thomas Heller
#
import unittest
from ctypes import *
from _ctypes_test import func_s_p

class Callbacks(unittest.TestCase):
    def test_callback(self):
        # define a callback function
        CALLBACK = CFUNCTYPE(c_int, c_int, c_int)
        def add(a, b):
            return a + b

        self.assertEqual(add(1, 2), 3)

        # register the callback function with a foreign function
        # calling convention
        func_s_p.restype = None
        func_s_p.argtypes = [CALLBACK, c_int, c_int]

        func_s_p(add, 2, 3)

    def test_errorfunc(self):
        # Test the error func
        func_s_p.restype = None
        func_s_p.argtypes = None

        # define an error function
        ERRORFUNC = CFUNCTYPE(None, c_char_
