import io
# Test io.RawIOBase
def _test_io_raw_iobase():
    class TestRawIO(io.RawIOBase):
        def read(self, len=None):
            return b'1' * len
        def write(self, b):
            pass
        def readable(self):
            return True
        def writable(self):
            return True
    TestRawIO().readable()
    TestRawIO().writable()
    TestRawIO().read(1)
    TestRawIO().write(b'1')

# Test io.BufferedIOBase
def _test_io_buffered_iobase():
    class TestBufferedIO(io.BufferedIOBase):
        def read(self, len=None):
            return b'1' * len
        def write(self, b):
            pass
        def raw(self):
            return TestRawIO()
        def flush(self):
            pass
        def read1(self, len=None):
            return b'1' * len
        def readable(self):
            return True
        def writable(self):
