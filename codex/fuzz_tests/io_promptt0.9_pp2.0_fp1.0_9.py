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
if n != 0:
    raise RuntimeError("wrong len")
if len(buf1) != 0:
    raise RuntimeError("buffer changed length")
if rawio.buf != b"hello":
    raise RuntimeError("buffer modified")

# Now read into a large enough buffer
buf2 = bytearray(10)
n = rawio.readinto(buf2
