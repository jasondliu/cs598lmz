import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase tests that are also valid for BufferedIOBase
class RawBufferedMixin:
    def test_detach(self):
        raw = self.RawIO()
        buf = self.BufferedIO(raw)
        buf.detach()
        self.assertEqual(buf.read(0), b'')
        self.assertRaises(ValueError, buf.detach)
        self.assertRaises(ValueError, buf.read, 1)
        self.assertRaises(ValueError, buf.write, b'')
        self.assertRaises(ValueError, buf.seek, 0)
        self.assertRaises(ValueError, buf.tell)
        self.assertRaises(ValueError, buf.flush)
        self.assertRaises(ValueError, buf.close)
        self.assertRaises(ValueError, buf.isatty)
        self.assertRaises(ValueError, buf.readable)
        self.assertRaises
