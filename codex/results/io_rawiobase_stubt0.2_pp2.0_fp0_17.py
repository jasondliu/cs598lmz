import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._seekable = True
        self._tell = 0
    def readable(self):
        return self._reading
    def writable(self):
        return self._writing
    def seekable(self):
        return self._seekable
    def readinto(self, b):
        data = self._file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n
    def write(self, b):
        n = self._file.write(b)
        self._tell += n
        return n
    def seek(self, offset, whence=io.SEEK_SET):
        if
