import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.pos = 0
    def read(self, size=None):
        if size is None:
            size = -1
        with open(self.name, 'rb') as f:
            f.seek(self.pos)
            data = f.read(size)
            self.pos = f.tell()
            return data
    def write(self, data):
        with open(self.name, 'r+b') as f:
            f.seek(self.pos)
            f.write(data)
            self.pos = f.tell()
    def seek(self, pos, whence=None):
        if whence is None:
            whence = io.SEEK_SET
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = os.stat(self.
