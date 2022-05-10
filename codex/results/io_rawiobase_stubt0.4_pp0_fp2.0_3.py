import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readinto(self, b):
        return os.read(self.fd, b)
    def close(self):
        return os.close(self.fd)

def open(file, mode="r"):
    return File(os.open(file, os.O_RDONLY))

def read(fd, n):
    return os.read(fd, n)

def write(fd, b):
    return os.write(fd, b)

def close(fd):
    return os.close(fd)

def seek(fd, pos, whence=0):
    return os.lseek(fd, pos, whence)

def tell(fd):
    return os.lseek(fd, 0, 1)

def truncate(fd, pos=None):
    if pos is None:
        pos = tell(fd)
    return os.ftruncate(fd, pos)

def size(fd):
    return os.fstat(fd)[6]
