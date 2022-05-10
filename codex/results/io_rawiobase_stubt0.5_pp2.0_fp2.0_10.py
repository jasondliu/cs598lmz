import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self._read = f.read
        self._seek = f.seek
        self._tell = f.tell
    def readinto(self, b):
        n = self._readinto(b)
        if n is None:
            n = self._read(b)
            n = len(n)
        return n

class StringIO(io.TextIOBase):
    def __init__(self, value=''):
        self._buf = io.BytesIO(value.encode('utf-8'))
    def read(self, n=-1):
        return self._buf.read(n).decode('utf-8')
    def write(self, s):
        return self._buf.write(s.encode('utf-8'))

class BytesIO(io.RawIOBase):
    def __init__(self, initial_bytes=None):
        self._buf = io.BytesIO(initial_bytes)
    def readinto(self, b):
        return self._
