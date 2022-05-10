import io
# Test io.RawIOBase by creating an in-memory stream
# that reads and writes bytes data.

# Create a RawIO implementation.
class BytesIOModel(io.RawIOBase):
    def __init__(self):
        self.buf = bytearray()
        self.pos = 0
    def readinto(self, b):
        n = min(len(self.buf) - self.pos, len(b))
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
    def write(self, b):
        n = len(b)
        newpos = self.pos + n
        if newpos > len(self.buf):
            self.buf[self.pos:] = b
        else:
            self.buf[self.pos:newpos] = b
        self.pos = newpos
        return n

# Test the RawIO implementation.
bytesio = BytesIOModel()

# Write some bytes.
n = bytesio.write(b"abcdef")
print
