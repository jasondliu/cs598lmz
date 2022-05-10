import io
# Test io.RawIOBase subclass, writing bytes to a BytesIO instance.

import _io
import unittest
import io
import pickle

from test import test_support

# A raw IO implementation that writes to a BytesIO instance

class BytesIOWriter(io.RawIOBase):

    def __init__(self):
        self._buffer = io.BytesIO()

    def write(self, b):
        self._buffer.write(b)
        return len(b)

    def getvalue(self):
        return self._buffer.getvalue()


class TestRawIO(unittest.TestCase):

    def test_rawiobase(self):
        rawio = BytesIOWriter()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self.assertRaises(io.UnsupportedOperation, rawio.readlines)
        self.
