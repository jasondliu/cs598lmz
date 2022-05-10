import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test readinto()
        self.assertEqual(io.RawIOBase.readinto(None, b""), 0)
        self.assertEqual(io.RawIOBase.readinto(None, bytearray(b"")), 0)
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, memoryview(b""))
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, "")
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, bytearray())
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, memoryview())
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, object())
        self.assertRaises(TypeError, io.RawIOBase.readinto, None, None)
        self.assertRaises(TypeError, io.RawIOBase.read
