import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.fd = os.open(name, mode)
    def close(self):
        if self.fd:
            os.close(self.fd)
            self.fd = None
    def fileno(self):
        return self.fd
    def isatty(self):
        return False
    def readable(self):
        return 'r' in self.mode
    def readinto(self, b):
        return os.read(self.fd, b)
    def readline(self, limit=-1):
        return io.RawIOBase.readline(self, limit)
    def seekable(self):
        return True
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)
    def writable(self):
        return 'w'
