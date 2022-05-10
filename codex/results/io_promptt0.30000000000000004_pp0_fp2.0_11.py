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
        self.assertEqual(f.readinto(buf), 3)
        self.assertEqual(buf, b"foobar")
        self.assertEqual(f.readinto(buf), 0)
        self.assertEqual(buf, b"foobar")
        self.assertEqual(f.readinto(buf, 2), 0)
        self.assertEqual(buf, b"foobar")
        self.assertEqual(f.readinto(memoryview(buf)), 0)
        self.assertEqual(buf, b"foobar")
        self.assertEqual(f.readinto(memoryview(buf), 2),
