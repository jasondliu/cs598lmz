import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readline(self):
        return b"hello"
r = RawI()
