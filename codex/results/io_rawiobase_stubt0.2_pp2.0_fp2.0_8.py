import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
        self.open()
    def open(self):
        self.fd = os.open(self.path, self.mode)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)
    def write(self, b):
        return os.write(self.fd, b)
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)
    def fileno(self):
        return self.fd
