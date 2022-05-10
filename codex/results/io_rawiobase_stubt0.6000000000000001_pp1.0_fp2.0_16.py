import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
        self.offset = 0
        self.size = 0
        self.fsize = 0
        self.open(path)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def open(self, path):
        self.file = open(path, "rb")
        self.fsize = os.fstat(self.file.fileno()).st_size

    def close(self):
        self.file.close()

    def readinto(self, b):
        if not self.file:
            raise OSError("File closed.")
        length = len(b)
        if self.offset >= self.size:
            return 0
        if self.offset + length > self.size:
            length = self.size - self.offset
        self.file.seek(self.offset + self.fsize - self.size)
        res = self.file.read
