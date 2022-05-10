import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):

    def test_readinto(self):
        # Test a concrete implementation
        data = b"abcdefghij"
        buf = bytearray(5)
        f = io.BytesIO(data)
        n = f.readinto(buf)
        self.assertEqual(n, 5)
        self.assertEqual(buf, data[:5])
        # Test the readinto() argument
        self.assertRaises(TypeError, f.readinto, memoryview(buf))
        # Test readinto() with a too-small buffer
        buf = bytearray(3)
        f.seek(0)
        self.assertRaises(ValueError, f.readinto, buf)
        f.seek(0)
        n = f.readinto(buf, 5)
        self.assertEqual(n, 3)
        self.assertEqual(buf, data[:3])
        # Test readinto() with a too-large n
        buf = bytearray(3)

