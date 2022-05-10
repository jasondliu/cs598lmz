import io
# Test io.RawIOBase for compatibility
try:
    io.RawIOBase.read()
except TypeError:
    pass
else:
    raise RuntimeError("io.RawIOBase.read() should take at least one argument")


class _RawIOBase(io.RawIOBase):
    def __init__(self, buf, read_mode):
        self._buf = buf
        self._read_mode = read_mode

    def readable(self):
        return self._read_mode

    def writable(self):
        return not self._read_mode

    def seekable(self):
        return True

    def readinto(self, b):
        return io.RawIOBase.readinto(self, b)

    def read(self, n=-1):
        return io.RawIOBase.read(self, n)

    def write(self, b):
        return io.RawIOBase.write(self, b)

    def seek(self, pos):
        return io.RawIOBase.seek(self, pos)

    def tell(self):
        return io.RawIOBase.tell
