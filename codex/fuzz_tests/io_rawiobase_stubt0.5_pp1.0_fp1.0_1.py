import io
class File(io.RawIOBase):
    def __init__(self, path: str, mode: str = 'r'):
        self.path = path
        self.mode = mode
        self.file = None
        self.pos = 0
        self.size = 0
        if mode in ['r', 'rb']:
            self.file = open(path, mode)
            self.size = os.path.getsize(path)
        elif mode in ['w', 'wb']:
            self.file = open(path, mode)
        elif mode in ['a', 'ab']:
            self.file = open(path, mode)
            self.size = os.path.getsize(path)
        self.file.seek(0, os.SEEK_SET)

    def read(self, n: int = -1):
        if n == -1:
            n = self.size - self.pos
        buffer = self.file.read(n)
        self.pos += len(buffer)
        return buffer

    def seek(self, offset: int, whence: int):
        if whence ==
