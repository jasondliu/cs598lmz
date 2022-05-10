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
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

class FileWrapper(object):
    def __init__(self, f):
        self.f = f
    def __getattr__(self, name):
        return getattr(self.f, name)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.f.close()

# --------------------------------------------------------------------
# file object

class FileIO(io.RawIOBase
