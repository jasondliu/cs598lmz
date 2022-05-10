import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.name = file.name
        self.closed = False
    def close(self):
        if self.closed:
            return
        self.closed = True
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return 'r' in self.mode
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
       
