import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode)
    def open(self, name, mode):
        self.fd = os.open(name, mode)
    def close(self):
        if self.fd is not None:
            if self.closefd:
                os.close(self.fd)
            self.fd = None
    def fileno(self):
        return self.fd
    def write(self, b):
        if self.fd is None:
            raise ValueError("I/O operation on closed file")
        return os.write(self.fd, b)
    def read(self, n=-1):
        if self.fd is None:
            raise ValueError("I/O operation on closed file")
        return os.read(self.fd, n)
    def seek(self, offset, whence=os.SEEK_SET):
        if self.
