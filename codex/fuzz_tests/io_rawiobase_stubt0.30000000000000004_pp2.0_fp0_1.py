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
        data = self._file.read(len(b))
        n = len(data)
        b[:n] = data
        return n

    def write(self, b):
        n = self._file.write(b)
        self._tell += n
        return n

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self._tell
        elif whence == io.SEEK_END:
            offset += self._file.size()
        self._tell = offset
        return self._tell

    def tell(self):
        return self._tell

    def flush(self):
        return

    def close(self):
        return

class FileIO
