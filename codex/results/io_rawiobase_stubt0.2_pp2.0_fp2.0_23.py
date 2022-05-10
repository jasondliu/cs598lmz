import io
class File(io.RawIOBase):
    """
    A file-like object that reads from a file-like object.
    """
    def __init__(self, file, offset, length):
        self.file = file
        self.offset = offset
        self.length = length
        self.pos = 0
        self.file.seek(self.offset)

    def read(self, size=-1):
        if size == -1:
            size = self.length - self.pos
        if size == 0:
            return b''
        if self.pos + size > self.length:
            size = self.length - self.pos
        self.pos += size
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            self.pos = self.length + offset
        else:
            raise ValueError('Invalid whence value
