import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.file = io.FileIO(name)
        self.encoding = 'utf-8'
        self.line_buffering = False
        self.name = name
        self.mode = 'r'
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def readline(self, limit=-1):
        return self.file.readline(limit)
    def readlines(self, hint=-1):
        return self.file.readlines(hint)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return False
    def close(self):
        return self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return
