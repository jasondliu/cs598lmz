import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number of bytes read."""
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = self.file.readinto(b)
        self.offset += l
        return l

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += len(self.file)
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True


def test():
    f = File(bytearray(b'abcdefghijklmnopqrst
