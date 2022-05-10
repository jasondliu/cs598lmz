import io
class File(io.RawIOBase):
    """Raw I/O implementation for file objects."""

    def __init__(self, file):
        self._file = file

    def close(self):
        self._file.close()

    def fileno(self):
        return self._file.fileno()

    def isatty(self):
        return self._file.isatty()

    ### Readline[s] is a little tricky, since it's heavily dependent on having a seekable file.
    # For now we're going to handle it by using our own buffering.
    def read(self):
        return self._file.read()

    def readable(self):
        return self._file.readable()

    def readline(self):
        return self._file.readline()

    def readlines(self):
        return self._file.readlines()

    def seek(self, offset, whence = 0):
        return self._file.seek(offset, whence)

    def seekable(self):
        return self._file.seekable()

    def tell(self):
        return self._file.tell()


