import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._file = open(filename, mode)
    def close(self):
        self._file.close()
    def read(self, size=-1):
        return self._file.read(size)
    def write(self, b):
        return self._file.write(b)
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def readable(self):
        return self._file.readable()
    def writable(self):
        return self._file.writable()
    def seekable(self):
        return self._file.seekable()
    def fileno(self):
        return self._file.fileno()
    def flush(self):
        return self._file.flush()
    def isatty(self):
        return self._file.isatty()
    def __enter__(self):
        return self
    def __exit__(self, exc
