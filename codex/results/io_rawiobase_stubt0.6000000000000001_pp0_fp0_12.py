import io
class File(io.RawIOBase):
    def __init__(self, file, mode = 'r', buffering = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None):
        if isinstance(file, str):
            self._file = open(file, mode, buffering, encoding, errors, newline, closefd, opener)
        else:
            self._file = file
    def close(self):
        self._file.close()
    def readable(self):
        return self._file.readable()
    def readinto(self, b):
        return self._file.readinto(b)
    def write(self, b):
        return self._file.write(b)
    def writable(self):
        return self._file.writable()
    def seekable(self):
        return self._file.seekable()
    def seek(self, offset, whence = 0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def flush(self):
        return self._file
