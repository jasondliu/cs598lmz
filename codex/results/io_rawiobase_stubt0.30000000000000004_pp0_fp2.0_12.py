import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._offset = 0
        self._size = os.path.getsize(file)
    def readinto(self, b):
        if not self._reading:
            raise OSError('File not open for reading')
        if self._offset >= self._size:
            return 0
        with open(self._file, 'rb') as f:
            f.seek(self._offset)
            chunk = f.read(len(b))
            b[:len(chunk)] = chunk
            self._offset += len(chunk)
            return len(chunk)
    def write(self, b):
        if not self._writing:
            raise OSError('File not open for writing')
        with open(self._file, 'rb+' if self._offset else 'wb') as f:
            if self._offset:
                f.seek
