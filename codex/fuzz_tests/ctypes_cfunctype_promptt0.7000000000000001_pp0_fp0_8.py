import ctypes
# Test ctypes.CFUNCTYPE functionality
from ctypes.test import need_symbol

import unittest

class CFunctionTypeTestCase(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic_function(self):
        cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(self.callback)
        res = cb(42)
        self.assertEqual(res, 42)
        self.assertEqual(self.got_args, (42,))

    def test_basic_function_multiple_args(self):
        cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(self.callback)
        res = cb(42, 43)
        self.assertEqual(res, 43)
        self.assertEqual(self.got_args, (42, 43))

    def test_basic_function_with_argtyes(self
