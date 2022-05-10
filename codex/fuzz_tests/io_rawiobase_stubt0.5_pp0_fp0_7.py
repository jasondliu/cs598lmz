import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
    def __del__(self):
        self.close()
    def readable(self):
        return True
    def readinto(self, b):
        if self.fd is None:
            self.fd = open(self.path, 'rb')
        return self.fd.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if self.fd is None:
            self.fd = open(self.path, 'rb')
        return self.fd.seek(offset, whence)
    def tell(self):
        if self.fd is None:
            self.fd = open(self.path, 'rb')
        return self.fd.tell()
    def writable(self):
        return False


class FileWriter(io.
