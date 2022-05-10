import io
# Test io.RawIOBase

import unittest
import os
from test import test_support
from io import RawIOBase, BlockingIOError


class TestRawIOBase(unittest.TestCase):

    def test_overridden_init(self):
        class C(RawIOBase):
            def __init__(self):
                pass
        self.assertRaises(TypeError, lambda: RawIOBase())
        self.assertRaises(TypeError, RawIOBase)

    def test_readinto(self):
        class MyIO(RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:] = b"xyz"
                return len(b)
        b = bytearray(5)
        self.assertEqual(MyIO().readinto(b), 3)
        self.assertEqual(b, b"xyz\0\0")
        self.assertRaises(TypeError, MyIO().readinto, memoryview(b'123'))
        self.assertRaises(TypeError, MyIO().read
