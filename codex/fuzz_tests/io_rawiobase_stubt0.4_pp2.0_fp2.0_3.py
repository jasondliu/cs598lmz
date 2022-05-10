import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.f = open(path, mode)
        self.path = path
        self.mode = mode
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def readline(self, size=-1):
        return self.f.readline(size)
    def readlines(self, hint=-1):
        return self.f.readlines(hint)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)
    def seekable(self):
        return self.f.seekable()
    def tell(self):
        return self.f.tell()
    def truncate(self, size=None):
        return self.f.truncate(size)
    def writable(self):
