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
        if whence == 1:
            pos += self._tell
        elif whence == 2:
            pos += self._file.size()
        self._file.seek(pos)
        self._tell = pos
        return self._tell
    def tell(self):
        return self._tell
    def close(self):
        self._file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
       
