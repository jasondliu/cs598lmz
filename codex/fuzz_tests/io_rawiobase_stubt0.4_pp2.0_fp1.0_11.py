import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.length = os.fstat(f.fileno()).st_size
        self.tell = 0

    def readinto(self, b):
        if self.tell >= self.length:
            return 0
        n = self.f.readinto(b)
        self.tell += n
        return n

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.tell = offset
        elif whence == 1:
            self.tell += offset
        elif whence == 2:
            self.tell = self.length + offset
        else:
            raise ValueError("invalid whence (%r, should be 0, 1 or 2)" % (whence,))
        return self.tell

    def tell(self):
        return self.tell

    def fileno(self):
        return self.f.fileno()

    def __enter__(self):
       
