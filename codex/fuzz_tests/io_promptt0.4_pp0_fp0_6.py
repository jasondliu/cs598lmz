import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
    def readinto(self, b):
        n = len(self.data)
        b[:n] = self.data
        self.data = b""
        return n

r = MyRawIO(b"hello")
print(r.read())
print(r.read())

# Test io.BufferedIOBase

class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def _fill_buffer(self, n):
        self._read_buf = self.raw.read(n)
        self._read_buf_len = len(self._read_buf)
    def read(self, n):
        if n < 0:
            n = self._read_buf_len
        if n <= self._read_buf_len:
            data = self._read_buf[:n]
            self._read_buf = self._read_buf
