import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r", buffering=-1):
        super().__init__()
        self._name = name
        self._mode = mode
        self._buffering = buffering
        self._closed = False
        self._handle = None
        self._open()
    def __del__(self):
        if not self._closed:
            self._close()
            self._closed = True
    def _open(self):
        self._handle = open(self._name, self._mode)
    def _close(self):
        self._handle.close()
    def close(self):
        if not self._closed:
            self._close()
            self._closed = True
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return self._handle.readinto(b)
    def write(self, b):
        return self._handle.write(b)
    def seek(self, offset, whence
