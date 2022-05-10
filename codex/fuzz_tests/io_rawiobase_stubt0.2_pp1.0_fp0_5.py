import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
        self.mode = None
        self.name = None
        self.closed = True
    def open(self, mode='rb'):
        if self.closed:
            self.fd = os.open(self.path, os.O_RDONLY)
            self.mode = mode
            self.name = self.path
            self.closed = False
        else:
            raise ValueError('I/O operation on closed file')
    def close(self):
        if not self.closed:
            os.close(self.fd)
            self.closed = True
    def fileno(self):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        return self.fd
    def readable(self):
        return True
    def readinto(self, b):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        return os.read(self.fd, b)
    def seekable(
