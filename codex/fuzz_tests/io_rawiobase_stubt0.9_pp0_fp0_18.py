import io
class File(io.RawIOBase):
    def __init__(self, file):
        self._io = file
        self._blocked = 0
        self._blocking = True
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return False
    def flush(self):
        return True
    def isatty(self):
        return False
    def close(self):
        self._io.close()
        return True
    def write(self, b):
        if self._blocked:
            r, w, x = select.select([], [self._io], [], 0)
            if r:
                raise OSError('The writable side of the file is ready for reading.')
            if not w:
                raise OSError('The writable side of the file is not ready.')
        if isinstance(b, int):
            b = bytes((b,))
        try:
            n = self._io.send(b)
        except OSError as e:
            if e.errno == err
