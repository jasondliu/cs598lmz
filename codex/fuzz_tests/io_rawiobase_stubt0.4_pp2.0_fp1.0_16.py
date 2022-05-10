import io
class File(io.RawIOBase):
    """
    A file-like object that reads from the file at the given path.
    """
    def __init__(self, path):
        self._path = path
        self._file = None

    def open(self):
        self._file = open(self._path, 'rb')

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    def readable(self):
        return True

    def readinto(self, b):
        return self._file.readinto(b)

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()


class BytesIO(io.RawIOBase):
    """
    A file-like object that reads from a bytes object.
    """
    def __init__(self, b):
        self._b = b
        self._offset = 0

    def readable
