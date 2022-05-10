import io
class File(io.RawIOBase):
    def __init__(self, fd):
        super().__init__()
        self._fd = fd
    def close(self):
        self._fd.close()
    def fileno(self):
        return self._fd.fileno()
    def readinto(self, b):
        return self._fd.readinto(b)
    def readable(self):
        return True
    def seekable(self):
        return False
    def writable(self):
        return False
</code>

