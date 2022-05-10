import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        self.file = io.open(path, mode, *args, **kwargs)
        self.i = 0
        self.mode = mode
        self.len = os.path.getsize(path)
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def readinto(self, b):
        self.i += len(b)
        return self.file.readinto(b)
    def write(self, b):
        self.i += len(b)
        return self.file.write(b)
    def seek(self, i, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            self.i += i
        elif whence == io.SEEK_END:
            self.i = self.len + i
        else:
            self.i = i
        return self
