import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.name = filename
        self._modes = {
            'r': 'rb',
            'w': 'wb',
        }
        if mode not in self._modes:
            raise ValueError("Unsupported mode: {!r}".format(mode))
        self.mode = mode
        self._fp = _ffi.NULL
        if mode == 'r':
            self._fp = _lib.open_file(self.name)
            if self._fp == _ffi.NULL:
                raise OSError("Failed to open file: {}".format(self.name))
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def read(self, size=-1):
        if self.closed or self.mode != 'r':
            raise ValueError("I/O operation on closed file")
        if size == -1:
            size = _FFI_READ_CHUNK
