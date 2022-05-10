import io
# Test io.RawIOBase.readinto and io.RawIOBase.write
class TestRawIO(unittest.TestCase):
    def test_readinto(self):
        b = bytearray(b"foobar")
        r = io.BytesIO(b)
        a = bytearray(len(b) + 2)
        n = r.readinto(a)
        self.assertEqual(n, len(b))
        self.assertEqual(a, b)
        self.assertEqual(a[-2:], b"\x00\x00")
        n = r.readinto(a)
        self.assertEqual(n, 0)
        n = r.readinto(a)
        self.assertEqual(n, 0)
        self.assertEqual(a, b)
        self.assertEqual(a[-2:], b"\x00\x00")
        r.close()
        self.assertRaises(ValueError, r.readinto, a)
        a = bytearray(len(b) + 2
