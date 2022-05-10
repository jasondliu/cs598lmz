import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def close(self):
        if self.f:
            self.f.close()
            self.f = None
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def flush(self):
        self.f.flush()
    def tell(self):
        return self.f.tell()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def __next__(self):
        return self.f.__next__()
    def __iter__(self):
        return self.f.__iter__()
    def __enter__(self):
        return self.f.__enter__()
    def __exit__(self, *args
