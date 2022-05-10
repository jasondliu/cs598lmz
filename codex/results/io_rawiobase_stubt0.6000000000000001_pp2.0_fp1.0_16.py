import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
        self.offset = 0

    def open(self):
        self.fd = os.open(self.path, os.O_RDONLY)
        self.offset = 0

    def close(self):
        if self.fd:
            os.close(self.fd)
            self.fd = None

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.offset = offset
        elif whence == os.SEEK_CUR:
            self.offset += offset
        else:
            raise ValueError("Unsupported whence value {}".format(whence))
        return self.offset

    def tell(self):
        return self.offset

    def read(self, size=-1):
        if size < 0:
            size = os.stat(self.path).st_size - self.offset
        os.lseek(self.fd, self.offset, os.SEEK_SET)
