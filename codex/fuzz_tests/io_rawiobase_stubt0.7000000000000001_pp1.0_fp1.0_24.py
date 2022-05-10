import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, closefd=True):
        self.fd = os.open(filename, mode)
    def close(self):
        os.close(self.fd)
    def readinto(self, b):
        l = os.read(self.fd, len(b))
        b[:len(b)] = l
        return len(b)
    def write(self, b):
        return os.write(self.fd, b)
    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)
    def tell(self):
        return os.lseek(self.fd, 0, 1)
    def fileno(self):
        return self.fd

class FileNonBlock(File):
    def fileno(self):
        fd = os.dup(self.fd)
        os.set_blocking(fd, False)
        return fd

class FileBuffered(File):
    def __init__(self, filename, mode, closefd=True):
