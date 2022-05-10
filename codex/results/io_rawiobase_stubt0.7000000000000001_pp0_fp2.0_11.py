import io
class File(io.RawIOBase):
    def __init__(self):
        self.fd = open('test', 'rb')
        self.pos = 0
        self.maxpos = os.stat('test').st_size
        self.buff = bytearray(0)

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            pos += self.pos
        elif whence == io.SEEK_END:
            pos += self.maxpos
        if pos > self.maxpos:
            raise ValueError('Invalid pos')
        self.pos = pos

    def tell(self):
        return self.pos

    def readable(self):
        return True

    def _read1(self, size):
        if self.pos >= self.maxpos:
            return b''
        if self.pos < self.fd.tell():
            self.fd.seek(self.pos)
            self.buff = bytearray(self.fd.read(1024*1024))
        if self.pos + size >= self.maxpos:

