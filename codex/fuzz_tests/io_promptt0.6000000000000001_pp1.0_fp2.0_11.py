import io
# Test io.RawIOBase.readinto()

class ReadIntoTest(unittest.TestCase):
    def test_readinto(self):
        # Read from an empty stream
        b = bytearray(10)
        f = io.BytesIO()
        self.assertEqual(f.readinto(b), 0)
        self.assertEqual(len(b), 10)
        self.assertEqual(b, b'\x00'*10)
        # Read from a non-empty stream
        f = io.BytesIO(b'\x01\x02\x03\x04')
        n = f.readinto(b)
        self.assertEqual(n, 4)
        self.assertEqual(b[:4], b'\x01\x02\x03\x04')
        self.assertEqual(b[4:], b'\x00'*6)
        # Read too many bytes
        f = io.BytesIO(b'\x01\x02\x03\x04')
        self.assertEqual(f.
