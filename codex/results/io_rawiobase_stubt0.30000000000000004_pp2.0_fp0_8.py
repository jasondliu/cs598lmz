import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.offset = 0
        self.size = 0
        self.open()

    def open(self):
        self.file = open(self.filename, "rb")
        self.size = os.stat(self.filename).st_size

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def readinto(self, b):
        if self.file:
            if self.offset < self.size:
                self.file.seek(self.offset)
                size = min(len(b), self.size - self.offset)
                b[:size] = self.file.read(size)
                self.offset += size
                return size
            else:
                return 0
        else:
            return 0

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
