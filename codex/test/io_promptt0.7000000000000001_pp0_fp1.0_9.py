import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b""

