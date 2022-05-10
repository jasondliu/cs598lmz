import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._fp = None
        self._pos = None
        self._size = None
        self._dirty = False
        self._readonly = False
        self._open()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __repr__(self):
        return '<%s %s>' % (type(self).__name__, self._path)

    def __str__(self):
        return '<%s %s>' % (type(self).__name__, self._path)

    def _open(self):
        raise NotImplementedError

    def _flush(self):
        raise NotImplementedError

    def _close(self):
        raise NotImplementedError

    def _read(self, size=-1):
        raise NotImplementedError

    def _write(self, data):

