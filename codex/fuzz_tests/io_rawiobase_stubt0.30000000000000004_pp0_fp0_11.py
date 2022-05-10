import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode, closefd)
    def open(self, name, mode='r', closefd=True):
        self.fd = os.open(name, os.O_RDONLY)
        self.name = name
        self.mode = mode
        self.closefd = closefd
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def fileno(self):
        return self.fd
    def seekable(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return False
    def readinto(self, b):
        return os.read(self.fd, b)
    def read(self, n=-1):
        return os.read(self.fd, n)
   
