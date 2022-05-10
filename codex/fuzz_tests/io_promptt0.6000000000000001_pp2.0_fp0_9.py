import io
# Test io.RawIOBase

# io.RawIOBase.read()

class TestRawIOBaseRead(unittest.TestCase):
    def test_read(self):
        f = io.BytesIO(b"test")
        self.assertEqual(f.read(1), b"t")
        self.assertEqual(f.read(), b"est")
        self.assertEqual(f.read(), b"")

    def test_read_negative_size(self):
        f = io.BytesIO(b"test")
        with self.assertRaisesRegex(ValueError, "count should be >= 0"):
            f.read(-1)

# io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):
    def test_readinto(self):
        f = io.BytesIO(b"test")
        b = bytearray(4)
        self.assertEqual(f.readinto(b), 4)
        self.assertEqual(b, b"test")
        self.assertEqual
