import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd

    def close(self):
        if self._closefd:
            self._file.close()

    def fileno(self):
        return self._file.fileno()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return 'r' in self._mode

    def writable(self):
        return 'w' in self._mode

    def seekable(self):
        return self._file.seekable()

    def readinto(self, b):
        return self._file.readinto(b)

    def read(self, n=-1):
        return self._file.read(n)

    def write(self, b):
        return self._file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell
