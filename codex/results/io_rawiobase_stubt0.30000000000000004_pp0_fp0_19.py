import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.f = None
    def __enter__(self):
        self.f = open(self.path, self.mode)
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()
    def read(self, size=-1):
        return self.f.read(size)
    def write(self, b):
        return self.f.write(b)
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()
    def readable(self):
        return self.f.readable()
    def writable(self):
        return self.f.writable()
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=0):
        return self.
