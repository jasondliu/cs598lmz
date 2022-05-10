import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.file = io.FileIO(name, mode)
    def read(self, n):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        return self.file.flush()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __repr__(self):
        return repr(self.file)
    def __str__(self):
        return str(self.file)
    def __
