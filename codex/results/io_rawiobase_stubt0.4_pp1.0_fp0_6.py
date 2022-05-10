import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00" * n
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def write(self, b):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def tell(self):
        return 0

class FileIO(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None

    def read(self, n=-1):
        if self.fd is None:
            self.fd = open(self.name, self.mode)
        return self.fd.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return True

    def write(self, b):
       
