import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Issue #11458: calling RawIOBase.read() should not raise a
        # NotImplementedError.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertEqual(MyRawIO().read(1), b'')

    def test_readall(self):
        # Issue #11458: calling RawIOBase.readall() should not raise a
        # NotImplementedError.
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertEqual(MyRawIO().readall(), b'')

    def test_readinto(self):
        # Issue #11458: calling RawIOBase.readinto() should not raise a
        # NotImple
