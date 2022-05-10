import io
class File(io.RawIOBase):
    def __init__(self, path, mode, buffering=0):
        self.file = io.FileIO(path, mode, buffering)
        self.path = path
        self.mode = mode
        self.name = path
        self.closed = False
    def close(self):
        self.file.close()
        self.closed = True
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
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def seekable(self):
        return self.file.seekable()
    def tell(self):
        return self.file.tell()
   
