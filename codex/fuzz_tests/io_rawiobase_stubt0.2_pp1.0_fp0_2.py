import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def fileno(self):
        return self.f.fileno()
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True

class FileWrapper(object):
    def __init__(self, f):
        self.f = f
    def __getattr__(self, name):
        return getattr(self.f, name)

def wrap_file(f):
    if isinstance(f, io
