import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        return n

class BufferedReader(io.BufferedReader):
    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE):
        io.BufferedReader.__init__(self, File(raw), buffer_size)
    def peek(self, n):
        if n < 0:
            n = self.DEFAULT_BUFFER_SIZE
        elif n > self.DEFAULT_BUFFER_SIZE:
            raise ValueError("cannot peek ahead more than one buffer")
        while len(self._peeked_bytes) < n:
            b = self.raw.read(n - len(self._peeked_bytes))
            if not b:
                break
            self._peek
