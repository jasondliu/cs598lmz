import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def fileno(self):
        return self.f.fileno()
    def seekable(self):
        return self.f.seekable()
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()
    @classmethod
    def open(cls, filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
        return File(open(filename, mode, buffering, encoding, errors, newline, closefd))

class FileIO(io.FileIO):
    def
