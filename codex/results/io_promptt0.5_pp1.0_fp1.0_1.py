import io
# Test io.RawIOBase
import io
import os
import sys
import unittest
import _pyio as pyio
import pickle
import tempfile

# A mixin class to provide tests that apply to both raw and buffered I/O.
class CommonRawIOBaseTests(object):

    def test_read_non_blocking(self):
        # Issue #11649: calling read() on a non-blocking stream should
        # return None if no data is available.
        stream = self.open(os.devnull, "rb", buffering=0)
        self.assertIsNone(stream.read())
        stream = self.open(os.devnull, "rb", buffering=1)
        self.assertIsNone(stream.read())

    def test_read(self):
        stream = self.open(os.devnull, "rb", buffering=0)
        self.assertEqual(b"", stream.read())
        stream = self.open(os.devnull, "rb", buffering=1)
        self.assertEqual(b"", stream.read())

    def
