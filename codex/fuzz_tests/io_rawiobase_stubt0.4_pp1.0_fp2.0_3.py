import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.fd = None
        self.closed = True
        self.open(name, mode)
    def open(self, name, mode):
        self.fd = os.open(name, mode)
        self.closed = False
    def close(self):
        if not self.closed:
            os.close(self.fd)
            self.closed = True
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __del__(self):
        self.close()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        os.lseek(self.fd, offset, whence)
    def read(self, n=-1):
        return os.read(self.fd,
