import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode, closefd)

    def open(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode, closefd)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def __del__(self):
        self.close()

    def fileno(self):
        return self.fd

    def isatty(self):
        return False

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def seek(self, offset,
