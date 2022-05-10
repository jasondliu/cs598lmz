import _struct
# Test _struct.Struct.unpack() with a format that allows padding.

import test.support
import unittest
import sys
import io

# Test that unpack() accepts a buffer argument (for compatibility
# with the Python standard library).

class TestBuffer(unittest.TestCase):
    def test_buffer(self):
        # struct.Struct.unpack() should accept a buffer argument (for
        # compatibility with the Python standard library).
        s = _struct.Struct('i')
        buf = io.BytesIO(b'abcd')
        self.assertEqual(s.unpack(buf.read(s.size)), (1633837924,))

    def test_buffer_consumed(self):
        # struct.Struct.unpack() should consume the buffer argument
        # (for compatibility with the Python standard library).
        s = _struct.Struct('i')
        buf = io.BytesIO(b'abcd')
        s.unpack(buf.read(s.size))
        self.assertEqual(buf.read(s.size), b'')

    def test_
