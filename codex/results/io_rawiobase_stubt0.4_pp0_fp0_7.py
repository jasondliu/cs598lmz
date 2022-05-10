import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, *args, **kwargs):
        self.file = open(filename, mode, *args, **kwargs)
    def close(self):
        return self.file.close()
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
    def seekable(self):
        return self.file.seekable()
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)
    def writable(self):
