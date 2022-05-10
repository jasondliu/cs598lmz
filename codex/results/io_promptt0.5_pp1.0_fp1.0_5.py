import io
# Test io.RawIOBase
class IOBaseTest(unittest.TestCase):
    def test_readinto(self):
        b = bytearray(b'abc')
        with io.BytesIO(b) as f:
            self.assertEqual(f.readinto(b), 3)
            self.assertEqual(b, b'abcabc')
            self.assertEqual(f.readinto(b), 0)
            self.assertEqual(b, b'abcabc')
        with io.BytesIO(b) as f:
            self.assertEqual(f.readinto(b, 1), 3)
            self.assertEqual(b, b'aabcbc')
            self.assertEqual(f.readinto(b, 1), 0)
            self.assertEqual(b, b'aabcbc')
        with io.BytesIO(b) as f:
            self.assertEqual(f.readinto(b, 1, 2), 2)
            self.assertEqual(b, b'aababc')
            self.assertEqual(
