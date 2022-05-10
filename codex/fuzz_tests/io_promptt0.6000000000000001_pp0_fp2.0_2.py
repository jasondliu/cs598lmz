import io
# Test io.RawIOBase.readinto()

# Test that readinto() returns the number of bytes read. Also test that
# readinto() correctly updates the file position.

class ReadintoTest(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"abc")

    def test_readinto_all(self):
        buf = bytearray(3)
        n = self.f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"abc")

    def test_readinto_part(self):
        buf = bytearray(2)
        n = self.f.readinto(buf)
        self.assertEqual(n, 2)
        self.assertEqual(buf, b"ab")

    def test_readinto_zero(self):
        buf = bytearray(0)
        n = self.f.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"")
