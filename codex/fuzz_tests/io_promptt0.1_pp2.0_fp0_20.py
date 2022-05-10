import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11459: io.RawIOBase should be a new-style class
        self.assertTrue(issubclass(io.RawIOBase, object))

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertRaises(TypeError, rawio.read)
        self.assertEqual(rawio.readinto_calls, 0)
        self.assertRaises(TypeError, rawio.read, 10)
        self.assertEqual(rawio.readinto_calls, 0)
        self.assertRaises(TypeError,
