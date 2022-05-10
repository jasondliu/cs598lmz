import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)
    def close(self):
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def readline(self, size=-1):
        return self.file.readline(size)
    def readlines(self, hint=-1):
        return self.file.readlines(hint)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def seekable(self):
        return self.file.seekable()
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)
    def writable(self):
        return
