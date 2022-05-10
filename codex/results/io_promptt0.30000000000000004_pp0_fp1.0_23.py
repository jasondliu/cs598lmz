import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
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
        self.assertEqual(buf, b"fooba")
        n = f.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"fooba")
        self.assertRaises(TypeError, f.readinto, memoryview(buf))
        self.assertRaises(TypeError, io.RawIOBase.readinto)
        self.assertRaises(TypeError, io.RawIOBase.readinto, f)
        self.assertRaises(TypeError, io.Raw
