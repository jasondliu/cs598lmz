import io
# Test io.RawIOBase by implementing an in-memory read/write file
class InMemoryFile(io.RawIOBase):
    def __init__(self):
        # File position
        self._pos = 0
        # File contents
        self._data = bytearray()

    def write(self, b):
        self._data += b
        return len(b)

    def readinto(self, b):
        n = len(b)
        if self._pos >= len(self._data):
            # Reading at end of file, return EOF
            return None
        if n > len(self._data) - self._pos:
            # Request more than we have left, fill buffer and return EOF
            n = len(self._data) - self._pos
            b[:n] = self._data[self.pos:self.pos + n]
            self._pos = len(self._data)
            return None
        b[:n] = self._data[self.pos:self.pos + n]
        self._pos += n
        return n

    def readable(self):
       
