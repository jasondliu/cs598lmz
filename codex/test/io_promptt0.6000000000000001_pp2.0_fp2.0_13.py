import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.pos = 0
    def read(self, n):
        print("read({})".format(n))
        r = self.name[self.pos:self.pos + n]
        self.pos += n
        return r
    def seek(self, pos):
        print("seek({})".format(pos))
        self.pos = pos
    def tell(self):
        print("tell()")
        return self.pos
    def write(self, s):
        print("write({})".format(s))
        pos = self.pos
        self.pos += len(s)
        self.name = self.name[:pos] + s + self.name[pos + len(s):]
    def close(self):
        print("close()")
        self.pos = 0
        self.name = ''

x = MyRawIO('abcdefg')
print(x.tell())
