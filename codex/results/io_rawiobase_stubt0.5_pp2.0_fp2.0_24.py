import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        super().__init__()
        self._file = file
        self._mode = mode

    def readinto(self, b):
        n = len(b)  # No need to trap for EINTR: we're not in a signal handler.
        if n == 0:
            return 0
        try:
            return self._file.readinto(b)
        except AttributeError:
            return os.read(self.fileno(), b)

    def readable(self):
        return 'r' in getattr(self._file, 'mode', self._mode)

    def writable(self):
        return 'w' in getattr(self._file, 'mode', self._mode)

    def seekable(self):
        return super().seekable() or hasattr(self._file, 'seek')

    def seek(self, offset, whence=os.SEEK_SET):
        if hasattr(self._file, 'seek'):
            return self._file.seek(offset, whence)
        return super
