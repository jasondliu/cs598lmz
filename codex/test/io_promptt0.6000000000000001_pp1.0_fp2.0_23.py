import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        assert type(b) is bytearray
        b[:] = b"hello world"
        return len(b)

b = bytearray(10)
MyRawIO().readinto(b)
