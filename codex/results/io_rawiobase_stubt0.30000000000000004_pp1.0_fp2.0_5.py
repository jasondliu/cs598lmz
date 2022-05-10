import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = open(path, 'rb')
        self.size = os.fstat(self.fd.fileno()).st_size
        self.pos = 0
        self.closed = False

    def read(self, size=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if self.pos >= self.size:
            return b''
        if size < 0:
            size = self.size - self.pos
        else:
            size = min(size, self.size - self.pos)
        self.pos += size
        return self.fd.read(size)

    def seek(self, offset, whence=0):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if whence == 0:
            if offset < 0:
                raise ValueError("Seeking negative position")
            self.pos = offset
        elif whence == 1:
            if offset < 0:
                raise Value
