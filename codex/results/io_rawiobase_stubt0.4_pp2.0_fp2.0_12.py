import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = io.open(name, mode)
        self.size = os.path.getsize(name)
        self.pos = 0
        self.closed = False
        self.softspace = 0

    def read(self, size=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if size < 0:
            return self.file.read()
        else:
            return self.file.read(size)

    def write(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.file.write(b)
        self.pos = self.file.tell()
        return len(b)

    def seek(self, pos, whence=0):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.file.seek(pos, whence)
        self.pos = self
