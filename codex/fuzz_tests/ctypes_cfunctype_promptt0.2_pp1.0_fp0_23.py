import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit more complex than the others, because it
# tests the creation of a ctypes callback function.
#
# The callback function is called from the C code, and the
# C code also checks the return value of the callback.
#
# The test passes if the callback is called, and the return
# value is correct.

import unittest
from ctypes import *

class CallbackTestCase(unittest.TestCase):
    def test_callback(self):
        # The callback function
        CALLBACKFUNC = CFUNCTYPE(c_int, c_int)
        def callback(arg):
            return arg * 5

        # The C code
        #
        # int callback(int arg) {
        #     return callbackfunc(arg);
        # }
        #
        # int test_callback(int arg) {
        #     int result;
        #     callbackfunc = func;
        #     result = callback(arg);
        #     callbackfunc = NULL;
        #     return result;
        # }
        from ctypes
