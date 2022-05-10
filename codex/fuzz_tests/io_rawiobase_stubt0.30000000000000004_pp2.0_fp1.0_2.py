import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._fd = None
        self._mode = None
        self._pos = 0
        self._size = 0
        self._closed = False
        self._open()
    def _open(self):
        self._fd = open(self.name, 'rb')
        self._mode = 'rb'
        self._size = os.fstat(self._fd.fileno()).st_size
    def close(self):
        if self._closed:
            return
        self._closed = True
        self._fd.close()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._pos = offset
        elif whence == io.SEEK_CUR:
            self._pos += offset
        elif whence == io.SEEK_END:
            self._pos
