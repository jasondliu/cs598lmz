import io
# Test io.RawIOBase.readinto

# This test checks that readinto() works correctly when the object's
# buffer is non-empty.

class MyIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        if self.pos >= len(self.buf):
            return 0
        n = min(len(b), len(self.buf) - self.pos)
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        raise io.UnsupportedOperation("write() not supported")

# Create a buffer that is longer than the system buffer size
buf = b"x" * (io.DEFAULT_BUFFER_SIZE + 1)

# Create a RawIO object with a non-empty buffer
rawio = MyIO(buf)

# Read the first byte of the buffer
b = bytearray(1)
