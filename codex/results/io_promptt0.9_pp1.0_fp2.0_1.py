import io
# Test io.RawIOBase derived class using io.FileIO
class FileIO(io.RawIOBase):
    def __init__(self, name, mode, fd):
        super().__init__()
        self.mode = mode
        self._fd = fd

    def __repr__(self):
        return '<FileIO {}>'.format(self.mode)

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def readinto(self, buf):
        n = len(buf)
        n = min(n, 10) # We will read only 10 bytes
        data = self._fd.read(n)

        if data == b'':
            return 0

        buf[:n] = data
        return n

    def write(self, b):
        self._fd.write(b)
        return len(b)

    def flush(self):
        # noinspection PyArgumentList
        return self._fd.flush()


