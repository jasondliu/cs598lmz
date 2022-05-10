import io
# Test io.RawIOBase.read(), io.BufferedIOBase.read()
# and io.BufferedIOBase.read1()

import io
import sys
import unittest
import weakref
import contextlib

from test import support


class UnseekableIO(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return None

class ReadTest(unittest.TestCase):
    def setUp(self):
        self.word = b"Hello world\n"
        self.large = b"x" * (sys.maxsize + 1)
        self.fp = io.BytesIO(self.word)

    def tearDown(self):
        self.fp.close()
        self.fp = None

    def test_read(self):
        eq = self.assertEqual
        f = self.fp
        eq(f.read(4), b"Hell")
        eq(f.read(0), b"")
        eq(f.read(100), b"o world\n")
        eq(f
