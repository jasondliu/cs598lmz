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


def test_readinto():
    for initial_bytes in (b'', b'abcd'):
        for n in range(len(initial_bytes) + 1):
            for offset in range(n + 1):
                bytearray_obj = bytearray(b' ' * offset + b'
