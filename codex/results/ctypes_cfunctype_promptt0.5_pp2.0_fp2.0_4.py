import ctypes
# Test ctypes.CFUNCTYPE by creating a callback function and passing it to a
# C function that calls it.

from ctypes import *
import unittest
from test import support

# callback function
CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int)

def callback(a, b):
    "Python callback function"
    return a * b

class CallbackTestCase(unittest.TestCase):

    def test(self):
        cbfunc = CALLBACKFUNC(callback)
        # load the dll and retrieve the function ptr
        dll = CDLL(support.findfile("_ctypes_test.dll"))
        func = dll.test_callback
        func.argtypes = (c_int, c_int, CALLBACKFUNC)
        func.restype = c_int

        # call the dll function
        result = func(2, 3, cbfunc)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
