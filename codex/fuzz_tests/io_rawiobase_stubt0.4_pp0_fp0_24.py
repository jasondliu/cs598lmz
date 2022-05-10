import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.buf = []
        self.offset = 0
        self.closed = False
        self.softspace = 0
    def close(self):
        self.closed = True
    def read(self, size=-1):
        if size < 0:
            size = len(self.buf)
        if size > len(self.buf) - self.offset:
            size = len(self.buf) - self.offset
        ret = b''.join(self.buf[self.offset:self.offset+size])
        self.offset += size
        return ret
    def readline(self, size=-1):
        ret = b''
        while True:
            if size > 0 and len(ret) >= size:
                break
            if self.offset >= len(self.buf):
                break
            ret += self.buf[self.offset]
            self.offset += 1
        return ret
    def write(self, data):
        self.buf.append
