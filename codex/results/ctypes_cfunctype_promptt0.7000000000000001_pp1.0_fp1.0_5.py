import ctypes
# Test ctypes.CFUNCTYPE.
#
# (PyArg_ParseTuple() is used to obtain the arguments because it
# lets us pass in either a tuple or an integer.)
#
# Written by Thomas Heller.

import unittest
from test import support

from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def test_simple_call(self):
        # Simple call of a CFuncPtr.
        f = CFUNCTYPE(c_int, c_int)(lambda x: x + 42)
        self.assertEqual(f(8), 50)

    def test_simple_call_with_tuple(self):
        # Simple call of a CFuncPtr with a tuple.
        f = CFUNCTYPE(c_int, c_int)(lambda x: x + 42)
        self.assertEqual(f((8,)), 50)

    def test_simple_call_with_integer(self):
        # Simple call of a CFuncPtr with an integer.
        f = CFUNCTYPE(c_int, c_int
