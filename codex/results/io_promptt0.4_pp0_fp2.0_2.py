import io
# Test io.RawIOBase

import _io
import unittest
import weakref

# Base class for testing RawIOBase.
class BaseTestRawIO(unittest.TestCase):
    def setUp(self):
        self.r = self.io.open(self.TESTFN, "w+b")

    def tearDown(self):
        if self.r:
            self.r.close()
        unlink(self.TESTFN)

    def test_attributes(self):
        self.assertTrue(self.r.readable())
        self.assertTrue(self.r.writable())
        self.assertFalse(self.r.seekable())
        self.assertEqual(self.r.name, self.TESTFN)
        self.assertEqual(self.r.mode, "w+b")

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, by
