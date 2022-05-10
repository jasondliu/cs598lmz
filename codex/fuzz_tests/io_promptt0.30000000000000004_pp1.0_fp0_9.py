import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(1), b"")

    def test_readinto(self):
        b = io.BytesIO(b"abc")
        buf = bytearray(2)
        n = b.readinto(buf)
        self.assertEqual(n, 2)
        self.assertEqual(buf, b"ab")
        n = b.readinto(buf)
        self.assertEqual(n, 1)

