import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.filename, self.mode)

    def close(self):
        self.file.close()

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return self.file.readinto(b)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def flush(self):
        return self.file.flush()

    def read(self, n=-1):
        return self.file.read(n)

    def readline(self, limit=-1):
        return self
