import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
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
            raise ValueError("Invalid value for whence: %r" % (whence,))
        return self.offset
    def tell(self):
        return self.offset
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        pass
    def close(self):
        if self.closed:
            return
        try:
            if hasattr(self.file, "close"):
                self.file.
