import io
class File(io.RawIOBase):
    """Class to wrap file objects.

    Implements the 'raw stream' interface.

    """
    def __init__(self, filename, mode="r"):
        self.name = filename
        self.mode = mode
        self.closed = False
        self._file = open(filename, mode)

    def close(self):
        self._file.close()
        self.closed = True

    def fileno(self):
        return self._file.fileno()

    def readable(self):
        return self.mode in ("r", "rb")

    def writable(self):
        return self.mode in ("w", "wb")

    def seekable(self):
        return True

    def readinto(self, b):
        return self._file.readinto(b)

    def write(self, b):
        return self._file.write(b)

    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

    def truncate(
