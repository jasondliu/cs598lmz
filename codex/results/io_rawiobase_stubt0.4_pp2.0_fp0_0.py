import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def flush(self):
        return self.f.flush()
    def readable(self):
        return self.f.readable()
    def writable(self):
        return self.f.writable()
    def seekable(self):
        return self.f.seekable()
    def __next__(self):
        return self.f.__next__()
    def __iter__(self):
        return self.f.__iter__()
    def __enter__(self):

