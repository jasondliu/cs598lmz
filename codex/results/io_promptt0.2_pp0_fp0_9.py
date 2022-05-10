import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test reading
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(1), b"a")
        self.assertEqual(f.read(2), b"bc")
        self.assertEqual(f.read(4), b"")
        self.assertEqual(f.read(), b"")
        self.assertEqual(f.read(1), b"")
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(-1), b"abc")
        self.assertEqual(f.read(), b"")
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(None), b"abc")
        self.assertEqual(f.read(), b"")
        f = io.BytesIO(b"abc")
        self.assertEqual
