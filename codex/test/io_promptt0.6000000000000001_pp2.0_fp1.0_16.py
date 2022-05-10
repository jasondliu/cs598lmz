import io
# Test io.RawIOBase.readinto()

class BytesIO(io.RawIOBase):

    def __init__(self, initial_bytes=b''):
        self._buffer = initial_bytes
        self._read_ptr = 0

    def readinto(self, b):
        n = len(b)
        if self._read_ptr + n > len(self._buffer):
            n = len(self._buffer) - self._read_ptr
            b = memoryview(b)[:n]
        b[:n] = self._buffer[self._read_ptr:self._read_ptr+n]
        self._read_ptr += n
        return n

    def write(self, b):
        n = len(b)
        self._buffer += b
        return n


