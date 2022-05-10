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
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def flush(self):
        self.f.flush()
    def close(self):
        self.f.close()

def _get_file_descriptor(f):
    if isinstance(f, io.RawIOBase):
        return f.fileno()
    elif isinstance(f, File):
        return f.fileno()
    elif isinstance(f, int):
        return f
    else:
        raise TypeError("Expected
