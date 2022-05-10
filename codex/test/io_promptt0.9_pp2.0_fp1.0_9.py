import io
# Test io.RawIOBase.readinto()
import io
import sys

class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.buf = b"hello"

    def readable(self):
        return True
    def readinto(self, buf):
        n = len(self.buf)
        buf[:n] = self.buf
        self.buf = b""
        return n
    def writable(self):
        return True
    def write(self, data):
        self.filename = data.decode()

rawio = MyRawIO()

# Try reading into a too small buffer
buf1 = bytearray()
n = rawio.readinto(buf1)
