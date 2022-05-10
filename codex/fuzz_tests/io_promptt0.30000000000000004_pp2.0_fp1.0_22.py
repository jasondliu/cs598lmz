import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

# A mixin for testing raw I/O
class BaseRawIOSharingTests:
    # File objects are shareable, even when they're not seekable.
    # This test checks that the file position is shared properly.
    def test_shareable(self):
        f = self.FileIO(support.TESTFN, 'w+')
        f.write(b'abcdefghijklmnopqrstuvwxyz')
        f.seek(0)
        f2 = f.__class__(f)
        self.assertEqual(f.tell(), f2.tell())
        f2.seek(10)
        self.assertEqual(f.tell(), f2.tell())
        f.seek(26)
        self.assertEqual(f.tell(), f2.tell())
        f2.seek(0)
        self.assertEqual(f.tell(), f2.tell())
        f.seek(
