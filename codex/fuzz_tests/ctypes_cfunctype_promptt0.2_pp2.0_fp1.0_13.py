import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the ctypes tutorial, section "Calling functions in
# shared libraries":
# http://docs.python.org/library/ctypes.html#calling-functions-in-shared-libraries

import unittest
from test import support

# The following function is defined in the test_ctypes.pyd module:
#
# int testfunc(int a, int b) {
#     return a + b;
# }

lib = ctypes.CDLL(support.TESTFN)

class CFuncPtrTestCase(unittest.TestCase):
    def test_CFUNCTYPE(self):
        # Create a prototype for the required function, and cast the
        # function pointer to this prototype.
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        testfunc = prototype((("testfunc", lib),))

        # Now we can call the function just as a normal Python function.
        self.assertEqual(testfunc(1, 2),
