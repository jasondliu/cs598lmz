import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
        self.open()
    def open(self):
        self.fd = open(self.path, self.mode)
    def close(self):
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
    def fileno(self):
        return self.fd.fileno()
    def isatty(self):
        return self.fd.isatty()
    def readable(self):
        return self.fd.readable()
    def writable(self):
        return self.fd.writable()
    def seekable(
