import io
class File(io.RawIOBase):
    def __init__(self, file, mode = 'r'):
        self._file = open(file, mode)

    def read(self, n = -1):
        return self._file.read(n)

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
        self._file.write(b)
        return len(b)

    def fileno(self):
        return self._file.fileno()

    def seek(self, pos, whence = 0):
        self._file.seek(pos, whence)

    def tell(self):
        return self._file.tell()

    def close(self):
        self._file.close()

    def __enter__(self):

