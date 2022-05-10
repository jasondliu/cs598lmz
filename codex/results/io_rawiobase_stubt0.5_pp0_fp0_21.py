import io
class File(io.RawIOBase):
    def __init__(self, name, mode, buffering=0):
        self._name = name
        self._mode = mode
        self._buffer = buffering
        self._buffering = buffering
        self._closed = False
        self._readable = False
        self._writable = False
        self._seekable = False
        if self._mode.startswith('r'):
            self._readable = True
        if self._mode.startswith('w'):
            self._writable = True
        if self._mode.startswith('a'):
            self._writable = True
        if self._mode.startswith('r'):
            self._seekable = True
        if self._mode.startswith('w'):
            self._seekable = True
        if self._mode.startswith('a'):
            self._seekable = True
        if self._mode.startswith('r'):
            self._readable = True
        if self._mode.startswith('w'):
            self._writable = True
        if
