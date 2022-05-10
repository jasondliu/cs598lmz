import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
        self.closed = False
    def close(self):
        if self.closed:
            return
        self.closed = True
        self.file.close()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        b[:n] = data
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.file.seek(0, 2) + offset
        else:
            raise ValueError("Invalid value for whence: %r"
