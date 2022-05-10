import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b"foo"
                return 3
        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(bytes(buf), b"foob\x00")
        self.assertEqual(f.readinto(buf), 0)
        self.assertRaises(TypeError, f.readinto, memoryview(buf))
        self.assertRaises(TypeError, io.RawIOBase.readinto, f)
        self.assertRaises(TypeError, io.RawIOBase.readinto)
        # readinto() should check for closed file
        f.close()
        self.assertRaises(ValueError, f.
