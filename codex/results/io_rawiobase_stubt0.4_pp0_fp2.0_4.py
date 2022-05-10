import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self._fd = os.open(filename, os.O_RDONLY)
        self._closefd = closefd
    def close(self):
        if self._closefd:
            os.close(self._fd)
    def fileno(self):
        return self._fd
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self._fd, b)
    def read(self, n=-1):
        return os.read(self._fd, n)
    def readline(self, limit=-1):
        return os.read(self._fd, limit)
    def seekable(self):
        return True
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self._fd, offset, whence)
    def tell(self):

