import io
# Test io.RawIOBase as a base class

import os, tempfile
import unittest

class RawIOBaseTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io, 'RawIOBase'))
        self.assertIsInstance(io.RawIOBase, type)

    def test_unsupported_operations(self):
        # File-like object with no underlying implementation
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def writable(self):
                return False
        raw = TestRawIO()
        self.assertRaises(TypeError, len, raw)
        self.assertRaises(TypeError, iter, raw)
        self.assertRaises(TypeError, next, raw)
        self.assertRaises(TypeError, raw.__next__)
        self.assertRaises(TypeError, raw.seek, 0, 0)
        self.assertRaises(TypeError, raw.fileno)
