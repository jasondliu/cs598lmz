import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
        self.mode = None
        self.closed = True
    def open(self, mode='rb'):
        self.mode = mode
        self.fd = os.open(self.name, os.O_RDONLY)
        self.closed = False
    def close(self):
        if not self.closed:
            os.close(self.fd)
            self.closed = True
    def fileno(self):
        return self.fd
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd, 0, 1)
    def readinto(self, b):
        return os.read(self.fd, b)

