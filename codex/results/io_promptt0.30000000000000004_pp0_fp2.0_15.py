import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        b = bytearray(b"abc")
        r = io.BytesIO(b"xyz")
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"xyz")
        self.assertEqual(r.tell(), 3)
        r.seek(0)
        b = bytearray(2)
        n = r.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"xy")
        self.assertEqual(r.tell(), 2)
        r.seek(0)
        b = bytearray(4)
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"xyz\x00")
        self.assertEqual(r.tell(), 3)
