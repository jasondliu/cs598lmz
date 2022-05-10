import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

class RawIOTest(unittest.TestCase):

    def test_read_into(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:3] = b"foo"
                return 3
        self.assertEqual(MyRawIO().readinto(bytearray(5)), 3)
        self.assertEqual(MyRawIO().readinto(bytearray(5)), 3)
        self.assertEqual(MyRawIO().readinto(bytearray(5)), 3)
        self.assertEqual(MyRawIO().readinto(bytearray(5)), 3)

    def test_readinto_error(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                raise OSError
        with self.assertRaises(OSError):
           
