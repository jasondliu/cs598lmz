import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        assert type(b) is bytearray
        b[:] = b"hello world"
        return len(b)

b = bytearray(10)
MyRawIO().readinto(b)
assert b == b"hello worl"

MyRawIO().readinto(b[5:])
assert b == b"hello world"

class MyBufferedRawIO(io.BufferedIOBase):
    def readinto(self, b):
        assert type(b) is bytearray
        b[:] = b"hello world"
        return len(b)

b = bytearray(10)
MyBufferedRawIO().readinto(b)
assert b == b"hello worl"

MyBufferedRawIO().readinto(b[5:])
assert b == b"hello world"
