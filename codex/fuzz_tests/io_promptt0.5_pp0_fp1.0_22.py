import io
# Test io.RawIOBase.readinto
import io
import _io
import os
import sys
import unittest


class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto_bad_args(self):
        class MyRawIO(_io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                return 0
        myio = MyRawIO()
        self.assertRaises(TypeError, myio.readinto)
        self.assertRaises(TypeError, myio.readinto, b"")
        self.assertRaises(TypeError, myio.readinto, bytearray(b""), 0, "")
        self.assertRaises(TypeError, myio.readinto, bytearray(b""), "")
        self.assertRaises(TypeError, myio.readinto, bytearray(b""), "", 0)
        self.assertRaises(TypeError, myio.readinto, bytearray(b""), 0, "", "")
        self
