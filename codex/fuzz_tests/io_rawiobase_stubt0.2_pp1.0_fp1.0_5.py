import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
    def __enter__(self):
        self.fd = open(self.path, self.mode)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()
    def read(self, size=-1):
        return self.fd.read(size)
    def write(self, b):
        return self.fd.write(b)
    def seek(self, offset, whence=0):
        return self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
    def flush(self):
        return self.fd.flush()
    def close(self):
        return self.fd.close()
    def fileno(self):
        return self.fd.fileno()
    def isatty(self):
        return self.fd.isatty()
    def readable(self):
       
