import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._seekable = True
        self._tell = 0
    def readinto(self, b):
        n = self._file.readinto(b)
        self._tell += n
        return n
    def write(self, b):
        n = self._file.write(b)
        self._tell += n
        return n
    def seek(self, pos, whence=0):
        if whence == 0:
            self._file.seek(pos, 1)
            self._tell = pos
        elif whence == 1:
            self._file.seek(pos, 1)
            self._tell += pos
        elif whence == 2:
            self._file.seek(0, 2)
            self._tell = self._file.tell() + pos
        else:
            raise ValueError("Invalid value for `whence`")
    def tell(
