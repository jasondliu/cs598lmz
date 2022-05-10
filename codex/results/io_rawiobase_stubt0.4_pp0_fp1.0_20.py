import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.f = open(filename, mode)
        self.buf = b''
        self.buf_size = 4096
        self.buf_len = 0
        self.pos = 0
        self.closed = False

    def close(self):
        self.f.close()
        self.closed = True

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.buf_len + offset
        self.f.seek(self.pos, 0)

    def tell(self):
        return self.pos

    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if self.pos &gt;= self.buf
