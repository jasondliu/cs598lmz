import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self._open()
    def __repr__(self):
        return '<{} {!r}, mode {!r}>'.format(
            self.__class__.__name__,
            self.name,
            self.mode)
    def _open(self):
        self.fd = os.open(self.name, self._flags())
    def _close(self):
        if self.closefd:
            os.close(self.fd)
    def __del__(self):
        if not self.closefd:
            print('not closing')
        self._close()
    def _flags(self):
        return os.O_RDONLY
    def readable(self):
        return self.mode == 'r'
    def writable(self):
        return self.mode in {'w', 'a'}
    def seekable(self):
        return True
