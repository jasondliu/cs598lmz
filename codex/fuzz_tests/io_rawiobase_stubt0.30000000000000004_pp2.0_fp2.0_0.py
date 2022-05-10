import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
    def open(self):
        self.fd = open(self.path, self.mode)
    def close(self):
        if self.fd:
            self.fd.close()
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def readinto(self, b):
        return self.fd.readinto(b)
    def write(self, b):
        return self.fd.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
    def flush(self):
        return self.fd.flush()
    def fileno(self):
        return self.fd.fileno()
    def isatty(
