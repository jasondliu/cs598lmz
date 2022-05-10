import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER.

from ctypes import *

import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_1(self):
        # simple function call, no args, no return value
        # prototype: void func(void);
        func = CFUNCTYPE(None)(("func", dll))
        func()

    def test_2(self):
        # simple function call, no args, with return value
        # prototype: int func(void);
        func = CFUNCTYPE(c_int)(("func", dll))
        res = func()
        self.assertEqual(res, 42)

    def test_3(self):
        # simple function call, with args, no return value
        # prototype: void func(int);
        func = CFUNCTYPE(None, c_int)(("func", dll))
        func(42)

    def test_4(self):
        # simple function call, with args, with return value
        # prototype: int func(
