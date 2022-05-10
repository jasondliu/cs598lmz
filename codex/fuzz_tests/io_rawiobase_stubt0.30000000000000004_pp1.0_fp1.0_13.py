import io
class File(io.RawIOBase):

    def __init__(self, filename):
        self._filename = filename
        self._file = None

    def open(self):
        self._file = open(self._filename, 'rb')

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    def readinto(self, b):
        return self._file.readinto(b)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

    def fileno(self):
        return self._file.fileno()

    def flush(self):
        pass

    def isatty(self):
        return False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc
