import io
class File(io.RawIOBase):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.path, "wb")

    def close(self):
        self.file.close()

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return True

    def write(self, b):
        self.file.write(b)
        return len(b)

    def writable(self):
        return True

    def seekable(self):
        return False

    def seek(self, offset, whence=io.SEEK_SET):
        raise io.UnsupportedOperation

    def tell(self):
        raise io.UnsupportedOperation

    def truncate(self, size=None):
        raise io.UnsupportedOperation

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        self.file.flush()

    def
