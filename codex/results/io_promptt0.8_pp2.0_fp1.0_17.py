import io
# Test io.RawIOBase class

import unittest
import tempfile
import os
import io

from test.support import TESTFN, unlink

TEST_SIZE = 100

class BufferedBytesIOTests(unittest.TestCase):

    def setUp(self):
        self.name = TESTFN
        unlink(self.name)
        self.f = open(self.name, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(self.name)

    def test_constructor(self):
        b = io.BufferedReader(io.BytesIO())
        self.assertEqual(0, b.tell())
        self.assertEqual(False, b.readable())
        self.assertEqual(True, b.writable())
        self.assertEqual(True, b.seekable())
        self.assertEqual(0, b.readinto(bytearray(10)))
        self.assertEqual(b"", b.read())
        self.assertEqual(0
