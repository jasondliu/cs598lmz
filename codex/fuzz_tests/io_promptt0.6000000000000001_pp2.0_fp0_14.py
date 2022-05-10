import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        b.seek(0)
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        self.assertEqual(b.read(1), b"")
        b.seek(0)
        self.assertEqual(b.read(), b"abc")
        self.assertEqual(b.read(), b"")
        b.seek(0)
        self.assertEqual(b.read(None), b"abc")
        self.assertEqual(b.read(None), b"")
        b.seek(0)
        self.assertEqual(b.read(-1), b
