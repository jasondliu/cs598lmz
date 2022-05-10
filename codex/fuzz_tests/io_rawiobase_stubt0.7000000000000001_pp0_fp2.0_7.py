import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.file.seek(self.offset)
        result = self.file.readinto(b)
        self.offset += result
        return result

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return False

    def seek(self, offset, whence=0):
        self.offset = offset

    def tell(self):
        return self.offset

    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.closed = True
