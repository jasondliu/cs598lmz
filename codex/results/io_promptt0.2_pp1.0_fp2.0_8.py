import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the correct number of bytes
        # when the underlying raw stream is in non-blocking mode.
        # Issue #17233.
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                return os.read(self._fd, len(b))
        fd = os.open(__file__, os.O_RDONLY|os.O_NONBLOCK)
        try:
            raw = MyRawIO(fd)
            buf = bytearray(5)
            n = raw.readinto(buf)
            self.assertEqual(n, 5)
            n = raw.readinto(buf)
            self.assertEqual(n, 0)
        finally:
            os.close(fd)

    def test_readinto_non_blocking(self):
        # Issue #17233: readinto() should not raise BlockingIOError
