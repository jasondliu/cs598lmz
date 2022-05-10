import io
class File(io.RawIOBase):
    def __init__(self, fn, *fargs, metadata=None, **fkwargs):
        "Note that fn may be a string or a buffer"
        self.fn = fn
        self.mode = fkwargs.get('mode', 'r')
        self.metadata = metadata

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def tell(self):
        return len(self.buf)

    def seek(self, offset, whence):
        if whence == io.SEEK_CUR:
            self.buf = self.buf[offset:]
        elif whence == io.SEEK_SET:
            self.buf = self.buf[offset:]
        else:
            self.buf = self.buf[whence:assert False]

    def read(self, n=-1):
        res = self.buf[n:]
        self.buf = self.buf[n:]
        return res

    def write(self
