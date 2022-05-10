import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode)
    def open(self, name, mode):
        self.fd = os.open(name, os.O_RDONLY)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def fileno(self):
        return self.fd
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)
    def read(self, n=-1):
        return os.read(self.fd, n)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd
