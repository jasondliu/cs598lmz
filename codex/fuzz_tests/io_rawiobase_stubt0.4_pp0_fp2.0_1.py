import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
    def close(self):
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def readline(self, n=-1):
        return self.file.readline(n)
    def readlines(self, n=-1):
        return self.file.readlines(n)
    def seek(self, n, whence=0):
        return self.file.seek(n, whence)
    def seekable(self):
        return self.file.seekable()
    def tell(self):
        return self.file.tell()
    def truncate
