import ctypes
# Test ctypes.CFUNCTYPE()

# NOTE: this test is not complete.  It is just a start.

import unittest

from ctypes import *

class CFuncTypeTestCase(unittest.TestCase):

    def test_argtypes(self):
        # The argtypes sequence is used to specify the types of the
        # arguments.  The types are checked when the function is called,
        # and must match exactly.  No conversions are done.

        # argtypes can be a tuple...
        CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)(1, 2)

        # ... or a list
        CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)(1, 2)

        # ... or any other sequence
        CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)(1, 2)

        # argtypes can be omitted, then the function is declared
        # without arguments
