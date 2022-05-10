import io
# Test io.RawIOBase

import io
import unittest
import weakref
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11459: _RawIOBase is an internal ABC, not meant for
        # subclassing.
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(1), b'')
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.read(10), b'')
        self.assertEqual(rawio.readinto_calls, 2)
        self.assertE
