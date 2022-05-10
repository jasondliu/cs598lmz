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
        self.assertEqual(buf, b"foo\x00\x00")
        self.assertEqual(f.readinto(buf), 0)
        self.assertRaises(TypeError, f.readinto, memoryview(buf))

    def test_read_into(self):
        # Test RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b"foo"
                return
