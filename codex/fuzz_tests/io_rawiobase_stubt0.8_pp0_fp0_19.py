import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.file = io.FileIO(*args, **kwargs)

    def read(self, n=-1):
        return self.file.read(n)

    def readable(self):
        return True

    def readinto(self, b):
        return self.file.readinto(b)

    def readall(self):
        return self.file.readall()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def seekable(self):
        return True

    def tell(self):
        return self.file.tell()

    def write(self, b):
        return self.file.write(b)

    def writable(self):
        return True

    def fileno(self):
        return self.file.fileno()

    def close(self):
        return self.file.close()

    def flush(self):
        return self.file.flush()


