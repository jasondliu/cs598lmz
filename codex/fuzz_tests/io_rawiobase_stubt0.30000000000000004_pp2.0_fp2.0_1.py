import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._file = None
    def open(self):
        self._file = open(self.name, 'rb')
    def close(self):
        self._file.close()
    def read(self, size=-1):
        return self._file.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def writable(self):
        return False
    def writelines(self, lines):
        raise io.UnsupportedOperation

class String(io.RawIOBase):
    def __init__(self, string):
        self._string = string
        self._pos = 0
    def read(self, size=-1):
        if size == -1:
            size = len(self._string)
        if self._pos + size > len(self
