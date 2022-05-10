import io
# Test io.RawIOBase

import _io

# A raw stream that produces bytes objects
class BytesRawIO(_io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buf = b""
    def readable(self):
        return True
    def readinto(self, b):
        count = len(b)
        if len(self.buf) - self.pos < count:
            count = len(self.buf) - self.pos
        b[:count] = self.buf[self.pos:self.pos+count]
        self.pos += count
        return count

# A raw stream that accepts bytes objects
class BytesRawIO(_io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buf = bytearray()
    def writable(self):
        return True
    def write(self, b):
        self.buf.extend(b)
        return len(b)


class ClosingTestCase(_io.BufferedIOBase):
    """Test the closing of streams
