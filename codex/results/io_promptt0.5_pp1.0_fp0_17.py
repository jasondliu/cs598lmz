import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_raw_io(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x00' * len(b)
                return len(b)
            def write(self, b):
                return len(b)
            def seekable(self):
                return False
            def readable(self):
                return True
            def writable(self):
                return True
        io.RawIOBase.__init__(TestRawIO())
        io.RawIOBase.close(TestRawIO())
        io.RawIOBase.fileno(TestRawIO())
        io.RawIOBase.isatty(TestRawIO())
        io.RawIOBase.read(TestRawIO(), 0)
        io.RawIOBase.seek(TestRawIO(), 0)
        io.RawIOBase.tell(TestRawIO())
        io.RawIOBase.truncate(TestRawIO(), 0)
        io.RawIOBase
