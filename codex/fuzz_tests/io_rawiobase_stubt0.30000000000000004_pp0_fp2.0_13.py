import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.closed = False
        self.fd = None
        self.open(name, mode)

    def open(self, name, mode):
        self.fd = os.open(name, os.O_RDONLY)

    def close(self):
        if self.closed:
            return
        self.closed = True
        os.close(self.fd)

    def fileno(self):
        return self.fd

    def readable(self):
        return True

    def readinto(self, b):
        return os.read(self.fd, b)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)

    def writable(self):
        return False

    def read(self,
