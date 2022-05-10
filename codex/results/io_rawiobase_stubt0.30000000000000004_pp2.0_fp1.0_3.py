import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fd = None
    def open(self):
        self.fd = os.open(self.filename, self.mode)
    def close(self):
        if self.fd:
            os.close(self.fd)
        self.fd = None
    def fileno(self):
        if self.fd is None:
            raise ValueError("I/O operation on closed file")
        return self.fd
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()
    def read(self, n=-1):
        if self.fd is None:
            raise ValueError("I/O operation on closed file")
        return os.read(self.fd, n)
    def write(self, b):
        if self.fd is None:
            raise ValueError("I/O operation on closed file")
        return os.write(self.fd, b)
