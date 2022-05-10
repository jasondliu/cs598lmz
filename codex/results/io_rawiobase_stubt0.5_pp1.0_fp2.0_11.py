import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = os.open(path, os.O_RDONLY)
        self.size = os.fstat(self.fd).st_size

    def read(self, size=-1):
        if size == -1:
            size = self.size - self.tell()
        return os.read(self.fd, size)

    def seek(self, offset, whence=io.SEEK_SET):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0, io.SEEK_CUR)

    def close(self):
        os.close(self.fd)

class FileBuffer(io.BufferedIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = os.open(path, os.O_RDONLY)
        self.size = os.fstat(self.fd).st_size
        self.buffer = b
