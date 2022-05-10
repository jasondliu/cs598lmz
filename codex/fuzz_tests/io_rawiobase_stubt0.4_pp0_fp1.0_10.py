import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(filename, mode)

    def open(self, filename, mode='r'):
        self.fd = os.open(filename, os.O_RDONLY)

    def close(self):
        if self.closefd:
            os.close(self.fd)
        else:
            self.fd = None

    def readable(self):
        return True

    def readinto(self, b):
        return os.read(self.fd, b)

class FileIO(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(filename, mode)

    def open(self, filename, mode='r'):
        self.fd =
