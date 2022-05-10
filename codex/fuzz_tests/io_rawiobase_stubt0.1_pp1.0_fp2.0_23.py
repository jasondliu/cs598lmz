import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def readable(self):
        return True
    def writable(self):
        return True
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

class FileWrapper(object):
    def __init__(self, f):
        self.f = f
    def __get
