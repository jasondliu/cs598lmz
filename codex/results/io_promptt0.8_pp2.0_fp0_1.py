import io
# Test io.RawIOBase interface for BytesIO objects

import io
import _io
import unittest

class BytesIOTests(unittest.TestCase):

    def setUp(self):
        self.bio = io.BytesIO()

    def test_read(self):
        self.assertRaises(TypeError, self.bio.read)
        self.assertEqual(b'', self.bio.read(0))
        self.assertRaises(io.BlockingIOError, self.bio.read, 1)
        self.bio.write(b'\x00\x01\x02')
        self.bio.seek(0)
        self.assertEqual(b'\x00', self.bio.read(1))
        self.assertEqual(b'\x01\x02', self.bio.read())
        self.assertEqual(b'', self.bio.read())

    def test_read1(self):
        self.assertRaises(TypeError, self.bio.read1)
        self
