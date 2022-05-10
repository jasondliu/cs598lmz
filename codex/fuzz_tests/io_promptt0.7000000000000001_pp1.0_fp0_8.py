import io
# Test io.RawIOBase
import os
import sys
import threading
import time
import unittest
from io import BytesIO, RawIOBase
from test import support
from test.support import (
    _4G, _4G + 1, _4G + 5, _TestIOBase, bigmemtest, bigaddrspacetest,
    findfile, requires_resource, run_with_locale, run_with_tz,
    threading_helper, unlink)
try:
    import thread
except ImportError:
    thread = None


class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        r = RawIOBase()
        self.assertRaises(IOError, r.read)
        self.assertRaises(IOError, r.readinto, bytearray())
        self.assertRaises(IOError, r.write, b"")

    def test_read_all_no_size(self):
        r = BytesIO(b"abcde")
        self.assertEqual(r.read(), b"abcde
