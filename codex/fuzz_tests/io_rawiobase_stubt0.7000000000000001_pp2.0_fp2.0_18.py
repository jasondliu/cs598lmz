import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self._fd = None

    def open(self):
        if self._fd is None:
          self._fd = os.open(self.path, os.O_RDONLY)
        return self._fd

    def readinto(self, b):
        fd = self.open()
        return os.read(fd, len(b))

    def close(self):
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None
</code>

