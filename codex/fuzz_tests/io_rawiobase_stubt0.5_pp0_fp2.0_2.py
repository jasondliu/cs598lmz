import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', **kwargs):
        self._path = path
        self._mode = mode
        self._handle = open(path, mode, **kwargs)
        self._buffer = b''
        self._buffer_pos = 0
        self._buffer_size = 0
        self._buffer_size_max = 4096
        self._buffer_size_min = 4096
        self._buffer_size_inc = 4096

    def __repr__(self):
        return '<{} path={!r} mode={!r}>'.format(type(self).__name__, self._path, self._mode)

    def readinto(self, b):
        if not self._buffer_size:
            self._buffer = self._handle.read(self._buffer_size_max)
            self._buffer_size = len(self._buffer)
            self._buffer_pos = 0
        if not self._buffer_size:
            return 0
        n = len(b)
        if n > self._buffer_size:
            n = self
