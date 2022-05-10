import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r", closefd=True):
        self.closefd = closefd
        self.fd = os.open(path, os.O_RDONLY)
        self.mode = mode
        self.name = path
        self.readable = "r" in mode
        self.writable = "w" in mode
        self.seekable = True
    def readinto(self, b):
        return os.read(self.fd, b)
    def read(self, n=-1):
        return os.read(self.fd, n)
    def write(self, b):
        return os.write(self.fd, b)
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)
    def close(self):
        if self.closefd:
            os.close(self.fd)
    def fileno
