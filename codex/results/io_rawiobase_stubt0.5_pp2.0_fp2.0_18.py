import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.mode = mode
        self.filename = filename
        self.fp = None
        self.open(filename, mode)
    def readable(self):
        return self.mode in {'r', 'r+', 'w+'}
    def writable(self):
        return self.mode in {'w', 'w+', 'r+'}
    def close(self):
        if self.fp:
            self.fp.close()
            self.fp = None
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    def open(self, filename, mode):
        if self.fp:
            self.close()
        self.fp = open(filename, mode)
    def seek(self, offset, whence=0):
        return self.fp.seek(offset, whence)
    def tell(self):
        return self.fp.tell()
    def fileno(self):
