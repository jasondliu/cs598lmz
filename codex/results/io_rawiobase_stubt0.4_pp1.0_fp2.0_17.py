import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode
        self.pos = 0
        self.file = None
        self.open()
    def open(self):
        if self.file is None:
            self.file = open(self.name, self.mode)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def read(self, size=-1):
        self.open()
        self.file.seek(self.pos)
        data = self.file.read(size)
        self.pos = self.file.tell()
        return data
    def seek(self, pos, whence=0):
        self.open()
        self.file.seek(pos, whence)
        self.pos = self.file.tell()
    def tell(self):
        self.open()
        return self.pos
    def seekable(self):
        return True
    def writable(self):
        return
