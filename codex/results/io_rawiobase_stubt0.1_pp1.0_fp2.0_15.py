import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._seekable = True
        self._tell = 0
        self._size = None
        if self._writing:
            self._size = 0
        elif self._reading:
            self._size = file.size()

    def readinto(self, b):
        if not self._reading:
            raise io.UnsupportedOperation("File was not opened for reading")
        l = len(b)
        data = self._file.read(self._tell, l)
        n = len(data)
        b[:n] = data
        self._tell += n
        return n

    def write(self, b):
        if not self._writing:
            raise io.UnsupportedOperation("File was not opened for writing")
        n = self._file.write(self._tell, b)
        self._tell += n
        self._size = max(
