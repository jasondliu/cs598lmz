import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        if not isinstance(file, io.RawIOBase):
            file = io.FileIO(file, mode)
        self.file = file
        self.mode = mode
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            size = os.fstat(self.file.fileno()).st_size
        if size == 0:
            return None
        b = self.file.read(size)
        self.pos += len(b)
        return b

    def readline(self):
        size = self.pos
        self.file.seek(0, 2)
        size = self.file.tell() - size
        self.file.seek(self.pos, 0)
        b = self.file.readline(size)
        self.pos += len(b)
        return b

    def readlines(self):
        size = self.pos
        self.file.seek(0, 2)
        size = self.file.
