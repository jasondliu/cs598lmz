import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def readinto(self, b):
        n = len(b)
        try:
            data = self.file.read(n)
            b[:len(data)] = data
            return len(data)
        except EOFError:
            return 0

class StringIO(io.RawIOBase):
    def __init__(self, string=""):
        self.buf = string
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        self.buf += b
        return len(b)

    def getvalue(self):
        return self.buf


