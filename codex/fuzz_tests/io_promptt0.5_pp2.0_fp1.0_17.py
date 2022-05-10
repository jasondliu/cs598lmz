import io
# Test io.RawIOBase

import _io
import unittest
from test import support

# The tests in this file are intended to exercise the io.RawIOBase
# interface.  The tests for RawIOBase implementations are in test_fileio,
# test_bytesio, and test_bufferedio.

# A test RawIOBase class.
class TestRawIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def write(self, b):
        pass


class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = TestRawIO()
        self.a = io.TextIOWrapper(self.f, encoding="ascii",
                                  line_buffering=True)

    def tearDown(self):
        self.a.close()
        self.f = None
        self.
