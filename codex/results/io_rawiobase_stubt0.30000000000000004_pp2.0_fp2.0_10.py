import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
        self.pos = 0

    def open(self):
        self.file = open(self.path, 'rb')
        self.pos = self.file.tell()

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def readable(self):
        return True

    def readinto(self, b):
        if self.file is None:
            self.open()
        l = self.file.readinto(b)
        self.pos = self.file.tell()
        return l

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = os.path.getsize(self.path) + pos
        else:
            raise ValueError("Invalid value for whence:
