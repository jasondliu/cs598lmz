import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.seek(0, io.SEEK_END) + offset
        else:
            raise ValueError("Invalid value for `whence`: %r" % (whence,))
        self.file.seek(self.offset)
        return self.offset
    def tell(self):
        return self.offset
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __enter__(self):
        return self
