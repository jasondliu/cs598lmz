import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()

class StringIO(io.StringIO):
    def __init__(self, s=''):
        self.buf = s
        self.len = len(s)
        self.buflist = []
        self.pos = 0
        self.closed = False
        self.softspace = 0
    def close(self):
        if not self.closed:
            self.closed = True
            del self.buf, self.pos
    def isatty(self):
        return False
    def seek(self, pos, mode=0):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        if mode == 1:
            pos += self.pos
        elif mode == 2:
            pos += self.len
