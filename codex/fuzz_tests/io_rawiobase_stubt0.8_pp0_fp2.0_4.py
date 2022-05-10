import io
class File(io.RawIOBase):

    def __init__(self, filename, mode='r', closefd=True):
        try:
            fd = _file.create(filename, mode, closefd)
        except (IOError, OSError) as e:
            if closefd:
                self.close = lambda: None
            raise
        io.RawIOBase.__init__(self)
        self._f = _io.FileIO(fd, closefd)
        self._close = closefd or mode[0] == 'a'
        self.mode = mode
        self.name = filename

    def close(self):
        if not self.closed:
            try:
                if self._close:
                    self._f.close()
            finally:
                del self._f
                io.RawIOBase.close(self)

    @property
    def closed(self):
        if not hasattr(self, "_f"):
            return True
        try:
            return self._f.closed
        except AttributeError:
            return True

    def fileno(self):
        self._f
