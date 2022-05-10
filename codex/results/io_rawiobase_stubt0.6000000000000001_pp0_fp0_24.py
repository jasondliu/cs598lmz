import io
class File(io.RawIOBase):
    if hasattr(os, 'fdopen'):
        def __init__(self, name, mode='r', closefd=True):
            self._closefd = closefd
            io.RawIOBase.__init__(self)
            self.name = os.path.abspath(name)
            self.mode = mode
            if closefd:
                self.fd = os.open(self.name, self.mode_int)
            else:
                self.fd = os.fdopen(os.open(self.name, self.mode_int), mode)
            self.readable = 'r' in self.mode
            self.writable = 'w' in self.mode
            self.seekable = True
        def close(self):
            if self._closefd:
                os.close(self.fd)
            else:
                self.fd.close()
        def __repr__(self):
            return "<%s.%s name=%r mode=%r closefd=%r>" % (
                self.__class__.__module__,

