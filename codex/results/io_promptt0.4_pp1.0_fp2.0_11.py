import io
# Test io.RawIOBase.readinto()

class TestReadinto(unittest.TestCase):

    def test_readinto(self):
        # Test that readinto() works as advertised.
        f = io.BytesIO(b"abc")
        b = bytearray(2)
        n = f.readinto(b)
        self.assertEqual(n, 2)
        self.assertEqual(b, b"ab")
        n = f.readinto(b)
        self.assertEqual(n, 1)
        self.assertEqual(b, b"c")
        n = f.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"c")

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer.
        f = io.BytesIO(b"abc")
        b = bytearray(2)
        n = f.readinto(b, 1)
        self.assertEqual(n, 2)
        self.assert
