import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', bufsize=-1):
        self._path = path
        self._mode = mode
        self._bufsize = bufsize
        self._file = None
        self._is_closed = False
        self._open()
    def _open(self):
        if self._file is None:
            self._file = open(self._path, self._mode, self._bufsize)
    def close(self):
        if not self._is_closed:
            self._file.close()
            self._is_closed = True
    def fileno(self):
        return self._file.fileno()
    def seek(self, offset, whence=0):
        self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def readable(self):
        return self._file.readable()
    def writable(self):
        return self._file.writable()
    def seekable(self):
        return self._file.seekable()
    def flush(self):

