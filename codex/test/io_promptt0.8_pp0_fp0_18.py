import io
# Test io.RawIOBase as a baseclass
class CustomIO(io.RawIOBase):
    def read(self, n=-1):
        return b'A' * n

with CustomIO() as f:
    d = f.read(10)
