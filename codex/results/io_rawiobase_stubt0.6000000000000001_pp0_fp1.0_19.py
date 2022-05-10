import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.encoding = 'utf-8'
        self.mode = 'r'
        self.name = file.name
        self.newlines = None
        self.softspace = 0
    def close(self):
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def seek(self, pos, whence = 0):
        self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def read(self, n = -1):
        return self.file.read(n)
    def readline(self, length = None):
        return self.file.readline(length)
    def readlines(self, sizehint = None):
        return self.file.readlines(sizehint)
    def truncate(self,
