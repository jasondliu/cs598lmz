import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        super(File, self).__init__(*args, **kwargs)
    def read(self, n=-1):
        return self._file.read(n)
    def close(self):
        self._file.close()
    def readable(self):
        return True
    def readinto(self, b):
        data = self._file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def writable(self):
        return False
    def write
