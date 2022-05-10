import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:3] = b"foo"
                return 3
        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"foob\x00\x00")
        self.assertEqual(f.readinto(buf), 0)
        self.assertEqual(buf, b"foob\x00\x00")
        self.assertRaises(TypeError, f.readinto, memoryview(buf))
        self.assertRaises(TypeError, io.RawIOBase.readinto, f, b"")
        self.assertRaises(TypeError, io.RawIOBase.readinto, f, bytearray())
        self.assertRaises(TypeError, io.RawIOBase.read
