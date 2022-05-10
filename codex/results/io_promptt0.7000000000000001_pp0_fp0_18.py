import io
# Test io.RawIOBase base class

import unittest
from test import support
from test.support import bigmemtest

class StrIO(io.StringIO):
    def write(self, s):
        self._check_closed()
        if not isinstance(s, str):
            raise TypeError("write() argument must be str, not %s" % s.__class__.__name__)
        return io.StringIO.write(self, s)

class BytesIO(io.BytesIO):
    def write(self, s):
        self._check_closed()
        if not isinstance(s, bytes):
            raise TypeError("write() argument must be str, not %s" % s.__class__.__name__)
        return io.BytesIO.write(self, s)

class AbstractRawIOBase(unittest.TestCase):
    def test_read(self):
        self.assertEqual(self.read(0), b"")
        self.assertRaises(TypeError, self.read, None)
        self.assertRaises(ValueError, self
