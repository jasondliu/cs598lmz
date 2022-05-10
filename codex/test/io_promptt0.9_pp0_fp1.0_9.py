import io
# Test io.RawIOBase
class RawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def close(self):
        pass
    def readinto(self, b):
        b[:] = b'x'*len(b)

# Test io.BufferedIOBase
