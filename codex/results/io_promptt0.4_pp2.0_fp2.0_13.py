import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        f = _io.BytesIO(b"abc")
        self.assertEqual(f.read(), b"abc")
        self.assertEqual(f.read(), b"")
        f = _io.BytesIO(b"abc")
        self.assertEqual(f.read(2), b"ab")
        self.assertEqual(f.read(2), b"c")
        self.assertEqual(f.read(2), b"")
        f = _io.BytesIO(b"abc")
        self.assertEqual(f.read(-1), b"abc")
        self.assertEqual(f.read(-1), b"")
        f = _io.BytesIO(b"abc")
        self.assertEqual(f.read(None), b"abc")
        self.assertEqual(f.read(None), b"")
        f = _io.BytesIO(b
