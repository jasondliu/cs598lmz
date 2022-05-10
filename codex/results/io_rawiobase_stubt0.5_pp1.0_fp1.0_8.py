import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', *args, **kwargs):
        self._filename = filename
        self._mode = mode
        self._args = args
        self._kwargs = kwargs
        self._file = None
        self._closed = True
    def open(self):
        if self._file is None:
            self._file = open(self._filename, self._mode, *self._args,
                              **self._kwargs)
        self._closed = False
    def close(self):
        if self._file is not None:
            self._file.close()
        self._closed = True
    def readable(self):
        return self._mode.startswith('r')
    def writable(self):
        return self._mode.startswith('w')
    def seekable(self):
        return True
    def _ensure_open(self):
        if self._closed:
            raise ValueError('I/O operation on closed file')
    def _ensure_readable(self):
        self._ensure_open
