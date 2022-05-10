import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self._file = io.FileIO(filename, mode)
        self.mode = mode
        self.name = filename

    def close(self):
        self._file.close()

    def fileno(self):
        return self._file.fileno()

    def flush(self):
        return self._file.flush()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return self._file.readable()

    def readinto(self, b):
        return self._file.readinto(b)

    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)

    def seekable(self):
        return self._file.seekable()

    def tell(self):
        return self._file.tell()

    def write(self, b):
        return self._file.write(b)

    def writable(self):
        return self._file.writable()

    def read(self
