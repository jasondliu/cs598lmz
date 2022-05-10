import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.fp = io.open(*args, **kwargs)
        self.name = self.fp.name
        self.encoding = self.fp.encoding
        self.mode = self.fp.mode
    def close(self):
        return self.fp.close()
    def fileno(self):
        return self.fp.fileno()
    def flush(self):
        return self.fp.flush()
    def isatty(self):
        return self.fp.isatty()
    def readable(self):
        return self.fp.readable()
    def readline(self, size=-1):
        return self.fp.readline(size)
    def readlines(self, hint=-1):
        return self.fp.readlines(hint)
    def seek(self, offset, whence=0):
        return self.fp.seek(offset, whence)
    def seekable(self):
        return self.fp.seekable()
    def tell(self):
        return
