import io
# Test io.RawIOBase subclass
class IOBaseTest(unittest.TestCase):
    def test_read(self):
        f = io.BytesIO(b"abc")
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(1), b"a")
        self.assertEqual(f.read(1), b"b")
        self.assertEqual(f.read(1), b"c")
        self.assertEqual(f.read(1), b"")
        self.assertEqual(f.read(), b"")
        self.assertEqual(f.read(1), b"")
        self.assertEqual(f.read(-1), b"")
        self.assertEqual(f.read(-1), b"")
        self.assertEqual(f.read(-2), b"")
        self.assertRaises(ValueError, f.read, -2)
        self.assertEqual(f.read(0), b"")
        self.assertEqual(f.read(),
