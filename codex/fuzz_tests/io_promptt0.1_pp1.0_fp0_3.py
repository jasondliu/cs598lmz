import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase subclasses that don't support tell().
class TellNotSupportedMixin:
    def test_tell(self):
        self.assertRaises(OSError, self.io.tell)

    def test_truncate_tell(self):
        self.assertRaises(OSError, self.io.truncate, 0)

# A mixin for RawIOBase subclasses that don't support seek().
class SeekNotSupportedMixin:
    def test_seek(self):
        self.assertRaises(OSError, self.io.seek, 0)

    def test_seekable(self):
        self.assertFalse(self.io.seekable())

    def test_truncate_seek(self):
        self.assertRaises(OSError, self.io.truncate, 0)

# A mixin for RawIOBase subclasses that don't support seek() or tell().
class UnseekableMixin(TellNotSupportedMixin, SeekNot
