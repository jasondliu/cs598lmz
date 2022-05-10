import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number of bytes read.
        If the object is in non-blocking mode and no bytes are available, None is returned.
        """
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = self.file.readinto(b)
        self.offset += l
        return l

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size()
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def read(self, n=-1):
        if self.closed
