import io
# Test io.RawIOBase

class RawIOBaseTest(unittest.TestCase):

    def test_read(self):
        # Test that read() calls readinto()
        class MyRawIO(io.RawIOBase):
            def readinto(self, buf):
                buf[:] = b'x' * len(buf)
                return len(buf)
        f = MyRawIO()
        self.assertEqual(f.read(5), b'xxxxx')
        self.assertEqual(f.read(), b'')

    def test_readinto(self):
        # Test that readinto() calls read()
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'x' * n
        f = MyRawIO()
        buf = bytearray(5)
        self.assertEqual(f.readinto(buf), 5)
        self.assertEqual(buf, b'xxxxx')
        self.assertEqual(f.readinto(buf), 0)
        self.assertEqual(buf, b
