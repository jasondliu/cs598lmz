import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.fd = None
        self.open()
    def open(self):
        self.fd = open(self.name, self.mode)
    def close(self):
        self.fd.close()
    def read(self, n):
        return self.fd.read(n)
    def write(self, b):
        return self.fd.write(b)
    def seek(self, offset, whence=0):
        return self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
    def flush(self):
        return self.fd.flush()
    def fileno(self):
        return self.fd.fileno()
    def isatty(self):
        return self.fd.isatty()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

