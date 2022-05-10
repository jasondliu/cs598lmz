import io
# Test io.RawIOBase

import os
import sys
import unittest
from test import support
from test.support import os_helper
from test.support import import_helper
from test.support import TESTFN
import io

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return 1
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(1), b'\0')
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.read(1), b'\0')
        self.assertEqual(rawio.readinto_calls, 2)

    def test_readall(self):
        # Test RawIOBase.readall()
        class Test
