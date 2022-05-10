import io
class File(io.RawIOBase):
    def __init__(self):
        super().__init__()
        self._buffer = bytearray()
        self._position = 0
        self._dirty = False
        self._is_closed = False
        self._file = None

    def __del__(self):
        self.close()

    def __repr__(self):
        return f"<memoryview {self._file}>"

    def read(self, size=-1):
        if self._file is not None:
            self._file.seek(self._position)
            result = self._file.read(size)
        else:
            result = self._buffer[self._position:self._position + size]
        self._position += len(result)
        return result

    def write(self, data):
        self._dirty = True
        self._buffer[self._position:self._position + len(data)] = data
        self._position += len(data)
        return len(data)

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.
