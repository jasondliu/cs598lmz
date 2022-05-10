import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', closefd=True):
        self._fd = os.open(path, os.O_RDONLY)
        self._closefd = closefd
    def close(self):
        if self._closefd:
            os.close(self._fd)
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self._fd, b)
    def seekable(self):
        return True
    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self._fd, offset, whence)
    def tell(self):
        return os.lseek(self._fd, 0, os.SEEK_CUR)
    def writeable(self):
        return False

def test():
    f = File('/etc/passwd')
    print(f.read(10))
    print(f.tell())
    print(f.seek(0))
    print(f.read(10))
    f.close()
