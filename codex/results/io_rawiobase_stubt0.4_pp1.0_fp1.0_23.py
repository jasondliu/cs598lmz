import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_RDONLY)
        self.size = os.fstat(self.fd).st_size
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            size = self.size
        if self.pos + size > self.size:
            size = self.size - self.pos
        if size == 0:
            return b''
        os.lseek(self.fd, self.pos, os.SEEK_SET)
        data = os.read(self.fd, size)
        self.pos += size
        return data

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.pos = offset
        elif whence == os.SEEK_CUR:
            self.pos += offset
        elif whence == os.SEEK_END:
            self.pos = self.size + offset
       
