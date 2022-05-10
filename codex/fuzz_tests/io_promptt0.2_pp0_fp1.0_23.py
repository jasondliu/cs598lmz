import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(), b"abc")
        self.assertEqual(b.read(), b"")

    def test_readinto(self):
        b = io.BytesIO(b"abc")
        buf = bytearray(2)
        n = b.readinto(buf)
        self.assertEqual(n, 2)
        self.assertEqual(buf, b"ab")
        n = b.readinto(buf)
        self.assertEqual(n, 1)
        self.assertEqual(buf[:1], b"c")
        self.assertEqual(buf[1:], b"b")
        n = b.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf[:1], b"c")
        self.assertEqual(buf[1:], b"
