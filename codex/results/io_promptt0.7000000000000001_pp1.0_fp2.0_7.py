import io
# Test io.RawIOBase using an in-memory bytes object

import _io
import io
import unittest

from test.support import TESTFN, run_unittest

test_string = b"abc\n123\ndef"


class RawIOMixin:

    def test_read(self):
        buf = self.buftype()
        self.assertEqual(self.f.readinto(buf), len(test_string))
        self.assertEqual(buf.getvalue(), test_string)
        self.assertRaises(ValueError, self.f.readinto, memoryview(buf))

    def test_fileno(self):
        self.assertRaises(UnsupportedOperation, self.f.fileno)

    def test_isatty(self):
        self.assertFalse(self.f.isatty())

    def test_seek(self):
        self.assertRaises(UnsupportedOperation, self.f.seek, 0, 0)

    def test_tell(self):
        self.assertRaises(UnsupportedOperation, self.f.tell)
