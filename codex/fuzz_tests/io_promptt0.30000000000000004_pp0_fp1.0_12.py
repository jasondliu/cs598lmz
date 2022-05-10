import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the correct number of bytes
        # read and that it does not modify the buffer past the
        # number of bytes read.
        for b in (b'', b'a', b'abc'):
            buf = bytearray(b'x' * len(b))
            f = io.BytesIO(b)
            n = f.readinto(buf)
            self.assertEqual(n, len(b))
            self.assertEqual(buf, bytearray(b + b'x' * (len(buf) - len(b))))
            f.close()

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer if it is too small.
        for b in (b'', b'a', b'abc'):
            buf = bytearray(1)
            f = io.BytesIO(b)
            n = f.readinto(buf)
            self
