import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        io.RawIOBase.__init__(self, *args, **kwargs)
    def readinto(self, b):
        return self._file.readinto(b)
    def read(self, n=-1):
        return self._file.read(n)
    def write(self, b):
        self._file.write(b)
        return len(b)
    def close(self):
        self._file.close()
    def seekable(self):
        return self._file.seekable()
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def __repr__(self):
        return repr(self._file)
    def __iter__(self):
        return iter(self._file)
    def __next__(self):
        return next(self._file)
    def __enter__(self):

