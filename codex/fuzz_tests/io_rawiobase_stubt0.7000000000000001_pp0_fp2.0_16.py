import io
class File(io.RawIOBase):
    __qualname__ = 'File'
    _size = None
    _closed = False
    def __init__(self, file, name, mode, closefd):
        self._file = file
        if closefd:
            self._closefd = True
        else:
            self._closefd = False
        self._name = name
        self._mode = mode
        self._io = io.BufferedIOBase()
        self._closed = False
        self._size = os.fstat(self._file.fileno()).st_size
    def fileno(self):
        self.check_closed()
        return self._file.fileno()
    def seekable(self):
        return self._file.seekable()
    def readable(self):
        return self._file.readable()
    def writeable(self):
        return self._file.writeable()
    def close(self):
        if self._closed:
            return
        self._closed = True
        if self._closefd:
            self._file.close()
    def flush(self):
       
