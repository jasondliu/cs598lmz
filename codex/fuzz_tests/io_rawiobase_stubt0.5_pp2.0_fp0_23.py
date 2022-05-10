import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.file) + offset
        else:
            raise ValueError("Invalid value for `whence`.")

    def tell(self):
        return self.offset

    def readinto(self, b):
        to_read = len(b)
        if self.offset >= len(self.file):
            return 0
        elif self.offset + to_read > len(self.file):
            to_read = len(self.file) - self.offset
        b[:to_read] = self.file[self.offset:self.offset + to_read]
        self.offset += to_read
        return to_read

    def readable(self):
        return True

    def seekable(self):
        return True

