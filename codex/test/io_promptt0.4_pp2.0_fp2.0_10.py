import io
# Test io.RawIOBase
import io
class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0
    def read(self, n):
        data = self.buf[self.offset : self.offset + n]
        self.offset += n
        return data
    def readable(self):
        return True

rawio = MyRawIO(b'abcdefghijklmnopqrstuvwxyz')

# Test io.BufferedIOBase
import io
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def _read_all(self):
        return self.raw.read()
    def readable(self):
        return True

bufferedio = MyBufferedIO(rawio)

# Test io.TextIOBase
import io
class MyTextIO(io.TextIOBase):
    def __init__(self, raw, encoding):
        self.raw = raw
