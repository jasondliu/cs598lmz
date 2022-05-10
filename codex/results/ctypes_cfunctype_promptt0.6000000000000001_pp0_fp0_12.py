import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):
    def test_basic(self):
        # prototype a function that takes two integers and returns an integer
        # by reference
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

        # now implement the function
        @prototype
        def func(arg1, arg2):
            arg2[0] = arg1 * 10
            return arg1 * arg2[0]

        # call the function
        result = func(3, ctypes.byref(ctypes.c_int()))
        self.assertEqual(result, 90)

    def test_errcheck(self):
        # prototype a function that takes two integers and returns an integer
        # by reference
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

       
