import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        self.name = file.name
        self.mode = file.mode
        self.encoding = file.encoding
        self.newlines = file.newlines
        self.softspace = file.softspace
    def read(self, n=-1):
        return self.file.read(n)
    def readline(self, length=None):
        return self.file.readline(length)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()
    def flush(self):
        return self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
   
