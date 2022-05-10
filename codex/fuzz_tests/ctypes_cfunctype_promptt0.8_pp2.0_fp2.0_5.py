import ctypes
# Test ctypes.CFUNCTYPE()
# create a 
import ctypes
import inspect
import os
import sys
import unittest

from test import mapping_tests
from test import support


class CtypesTests(unittest.TestCase):

    def test_callback_with_error(self):
        # c_int32 is callable and raises an error when called
        c_int32 = ctypes.c_int32

        with self.assertRaises(TypeError) as cm:
            c_int32(1)

        self.assertTrue(('expected c_int32 instance instead' in
                     cm.exception.args[0]) or
                    ('expected c_int32 instead' in
                     cm.exception.args[0]))

        # pass c_int32 to CFUNCTYPE, creating a new type that can be called
        # (and will return an int)
        Cf = ctypes.CFUNCTYPE(ctypes.c_int, c_int32)
        self.assertEqual(Cf(c_int32(1)), 1)
        # trying to call
