import io
class File(io.RawIOBase):
    """
    Wrapper for a file descriptor.
    """
    def __init__(self, path: str, mode: str = 'r'):
        self.fd = os.open(path, os.O_RDONLY)
        self.orig_path = path
        self.mode = mode
        self.name = path

    def close(self):
        os.close(self.fd)

    def readable(self):
        return self.fd >= 0 and bool(os.O_RDONLY & self.mode)

    def readinto(self, b):
        return os.read(self.fd, b)

    def readall(self):
        return os.read(self.fd, os.SEEK_END)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)


def mount(path: str):
   
