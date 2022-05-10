import io
class File(io.RawIOBase):
    def __init__(self, name, mode = 'r', closefd = True):
        if isinstance(name, int):
            name = str(name)
        if not isinstance(name, str):
            raise TypeError("invalid file: %r" % name)
        if not isinstance(mode, str):
            raise TypeError("invalid mode: %r" % mode)
        io.RawIOBase.__init__(self)
        self.mode = mode
        self.name = name
        self.closefd = closefd
        if not closefd:
            raise NotImplementedError("can't use closefd=False with this implementation")
        self._open()
    def __repr__(self):
        s = repr(self.name)
        if self.closed:
            s += ' (closed)'
        return '<_io.File%s>' % s
    def close(self):
        if self.closed:
            return
        io.RawIOBase.close(self)
        if self.closefd:
            if not hasattr
