import io
# Test io.RawIOBase.readinto()

# Test that readinto() returns the correct number of bytes read.
class TestReadinto(unittest.TestCase):
    def setUp(self):
        self.r = io.BytesIO(b'abcdefghij')

    def test_readinto_full(self):
        b = bytearray(5)
        self.assertEqual(self.r.readinto(b), 5)
        self.assertEqual(b, b'abcde')

    def test_readinto_bytearray(self):
        b = bytearray(5)
        self.assertEqual(self.r.readinto(b), 5)
        self.assertEqual(b, b'abcde')

    def test_readinto_memoryview(self):
        b = memoryview(bytearray(5))
        self.assertEqual(self.r.readinto(b), 5)
        self.assertEqual(b, b'abcde')

    def test_readinto_partial(self):
        b = byt
