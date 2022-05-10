import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into the writable buffer *b* and return
        the number of bytes read.  If the current file position is at the
        end of the file, returns 0.
        """
        self.file.seek(self.offset)
        result = self.file.readinto(b)
        self.offset += result
        return result

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size + offset
        return self.offset

    def tell(self):
        return self.offset

    def read(self, n=-1):
        self.file.seek(self.offset)
        result = self.file.
