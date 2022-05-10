import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.closed = False
        self.pos = 0
        self.file = None
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def close(self):
        if not self.closed:
            self.closed = True
            if self.file:
                self.file.close()
    def fileno(self):
        if not self.file:
            self.file = open(self.path, self.mode)
        return self.file.fileno()
    def readable(self):
        return 'r' in self.mode
    def readinto(self, b):
        if not self.file:
            self.file = open(self.path, self.mode)
        return self.file.readinto(b)
    def seek(self, pos, whence=io.SEEK_SET):
        if not self.file:
            self.file
