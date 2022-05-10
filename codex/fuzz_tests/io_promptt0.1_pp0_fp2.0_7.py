import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase subclasses that don't support tell() and seek().
class NoTell(object):
    def test_no_tell(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.tell, self.IO())

    def test_no_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, self.IO(), 0)

# A mixin for RawIOBase subclasses that don't support seek().
class NoSeek(object):
    def test_no_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, self.IO(), 0)

# A mixin for RawIOBase subclasses that don't support read().
class NoRead(object):
    def test_no_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.read, self.IO(), 0)

# A mixin for RawIOBase
