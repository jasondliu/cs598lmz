import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = len(b) # We're supposed to return at most this much
        chunk = self.file.read(l)
        n = len(chunk)
        b[:n] = chunk
        self.offset += n
        return n

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size
        self.offset = offset
        return self.offset

    def tell(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        return self.offset

