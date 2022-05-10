import io
class File(io.RawIOBase):
    def read(self, n=-1):
        if n == 0:
            return b''
        while True:
            b = self._read_block()
            if not b:
                break
            if n < 0:
                yield b
            else:
                yield b[:n]
                n -= len(b)
                if n <= 0:
                    break
    def readinto1(self, b):
        while True:
            data = self._read_block()
            if not data:
                break
            n = min(len(data), len(b))
            b[:n] = data[:n]
            if len(b) == n:
                break
            b = b[n:]
        return len(b)
    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                # The object does not expose writable
