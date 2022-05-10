import io
# Test io.RawIOBase

class TestRawIOBase:
    class MockRawIO(io.RawIOBase):
        def readable(self):
            return True

        def writable(self):
            return True

        def seekable(self):
            return True

        def readinto(self, buf):
            return len(buf)

        def write(self, buf):
            return len(buf)

        def seek(self, pos, whence):
            return 0

        def tell(self):
            return 0

        def read(self, n=-1):
            return b"0"

        def readall(self):
            return b"0"

        def read1(self, n=-1):
            return b"0"

        def close(self):
            pass

    def test_attributes(self):
        rawio = self.MockRawIO()
        assert rawio.mode == 'wb+'

    def test_io_methods(self):
        rawio = self.MockRawIO()

        # test read()
