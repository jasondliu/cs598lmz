import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode

    def read(self, n=-1):
        return self._file.read(n)

    def write(self, b):
        return self._file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

    def close(self):
        return self._file.close()

    def flush(self):
        return self._file.flush()

    def fileno(self):
        return self._file.fileno()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return 'r' in self._mode

    def writable(self):
        return 'w' in self._mode

    def seekable(self):
        return True

    def __next__(self):
        return self._file.__next__()
