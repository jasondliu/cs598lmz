import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number of bytes read."""
        if self.closed:
            raise ValueError("read from closed file")
        l = self.file.readinto(b)
        self.offset += l
        return l

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset = self.offset + offset
        elif whence == io.SEEK_END:
            offset = self.file.size() - offset
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def __repr__(self):
        return "<WasmFile %r>" % self.file


class WasmFile(File):
    def __init__
