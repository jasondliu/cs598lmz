import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(1), b"")
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(-1), b"abc")
        self.assertEqual(b.read(), b"")
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(None), b"abc")
        self.assertEqual(b.read(), b"")
        b = io.BytesIO(b"abc")

