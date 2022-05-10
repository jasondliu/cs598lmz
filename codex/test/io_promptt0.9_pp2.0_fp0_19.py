import io
# Test io.RawIOBase

# Base class for io.BytesIO
class MockRawIO(io.RawIOBase):
    def close(self):
        self.closed = True
    def seek(self, pos, whence=0):
        return 42
    def tell(self):
        return 42
    def truncate(self, pos=None):
        pass
    def flush(self):
        pass

class DuplexMockRawIO(MockRawIO):
    def write(self, b):
        pass

