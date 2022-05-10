import io
# Test io.RawIOBase.read()

import _io
import unittest
import weakref

from test.support import run_unittest, unlink

TESTFN = "test"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.rawio = self.theclass(TESTFN, "w+b")
        self.f = open(TESTFN, "w+b")

    def tearDown(self):
        self.rawio.close()
        self.f.close()

    def test_read(self):
        self.f.write(b"abc")
        self.f.flush()
        self.f.seek(0)
        self.assertEqual(self.rawio.read(2), b"ab")
        self.assertEqual(self.rawio.read(0), b"")
        self.assertEqual(self.rawio.read(1), b"c")
        self.assertEqual(self.rawio.read(), b"")

    def test_read_non_blocking(
