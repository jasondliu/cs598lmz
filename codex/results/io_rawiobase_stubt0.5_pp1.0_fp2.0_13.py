import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._offset = 0

    def readinto(self, b):
        if not self._reading:
            raise io.UnsupportedOperation("not reading")
        l = len(b)
        chunk = self._file.read(l)
        n = len(chunk)
        try:
            b[:n] = chunk
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', chunk)
        self._offset += n
        return n

    def write(self, b):
        if not self._writing:
            raise io.UnsupportedOperation("not writing")
        self._file.write(b)
        self._offset += len(b)
        return len(b)

    def seek(self, offset, whence=io.
