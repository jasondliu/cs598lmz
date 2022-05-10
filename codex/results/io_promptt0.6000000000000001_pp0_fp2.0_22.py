import io
# Test io.RawIOBase.readinto() for various read sizes
# This function is used to implement io.BufferedReader.readinto()
import io
import random
import sys
import unittest
from test import support
from test.support.script_helper import assert_python_ok

class RawIO_ReadintoTest(unittest.TestCase):

    def _test_readinto(self, rawio, b):
        # readinto() with various read sizes
        self.assertEqual(len(b), rawio.readinto(b))
        self.assertEqual(len(b), rawio.readinto(b))
        self.assertEqual(len(b) - 1, rawio.readinto(b))
        self.assertEqual(len(b) - 2, rawio.readinto(b))
        self.assertEqual(0, rawio.readinto(b))

    def test_readinto(self):
        # Issue #10061: readinto() with various read sizes
        b = bytearray(b' ' * 100)
        rawio = io.Bytes
