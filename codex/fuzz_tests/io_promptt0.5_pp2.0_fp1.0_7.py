import io
# Test io.RawIOBase.readinto

import _io
from test.support import run_unittest, import_module
from test.support.script_helper import assert_python_ok
import unittest
import os
import sys

class TestRawIOBase(unittest.TestCase):
    @unittest.skipUnless(hasattr(_io.RawIOBase, 'readinto'),
                         'requires RawIOBase.readinto')
    def test_readinto(self):
        # Test that readinto() works properly.
        #
        # Note: we should really test all objects that claim to implement
        # RawIOBase, but for now just test the builtin open() function.

        # Test readinto() with a bytearray
        with open(__file__, 'rb') as f:
            b = bytearray(10)
            n = f.readinto(b)
            self.assertEqual(n, 10)
            self.assertEqual(b, b'import _io')

            # Test readinto() with a memoryview
            b = bytearray(
