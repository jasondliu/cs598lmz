import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()
    def fileno(self):
        return self.file.fileno()
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return True
    def write(self, b):
        return self.file.write(b)
    def __enter__(self):
        self.file = open(self.filename, "rb")
        return self
    def __exit__(self, exc_type, exc
