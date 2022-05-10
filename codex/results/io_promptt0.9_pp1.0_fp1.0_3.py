import io
# Test io.RawIOBase

import unittest
from test import support

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        self.rawio = io.RawIOBase()

    def tearDown(self):
        self.rawio.close()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.rawio.read)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.rawio.write, '')

    def testReadinto(self):
        b = bytearray(5)
        res = self.rawio.readinto(b)
        self.assertEqual(res, 0)
        self.assertEqual(len(b), 5)
        self.assertEqual(b, b'\0'*5)

        b = bytearray(0)
        res = self.rawio.readinto(b)
        self.assertEqual(res, 0)
        self.assertEqual(len(b), 0)
