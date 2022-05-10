import io
# Test io.RawIOBase
import os
import os.path
import sys
import unittest
import warnings

from test import support
from test.support import script_helper
from test.support.script_helper import assert_python_failure

class TestRawIO(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO(b"1234567890")

    def test_read(self):
        b = self.f.read(5)
        self.assertEqual(b, b"12345")
        b = self.f.read(1000)
        self.assertEqual(b, b"67890")
        b = self.f.read(1000)
        self.assertEqual(b, b"")

    def test_readall(self):
        b = self.f.readall()
        self.assertEqual(b, b"1234567890")

    def test_readinto(self):
        b = bytearray(10)
        n = self.f.readinto(b)
        self
