import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def readline(self, n):
        return self.f.readline(n)
    def readlines(self, n):
        return self.f.readlines(n)
    def write(self, s):
        return self.f.write(s)
    def writelines(self, s):
        return self.f.writelines(s)
    def seek(self, n):
        return self.f.seek(n)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def __enter__(self):
        return self.f.__enter__()
    def __exit__
