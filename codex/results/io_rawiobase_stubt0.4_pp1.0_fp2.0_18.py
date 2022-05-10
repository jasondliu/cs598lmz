import io
class File(io.RawIOBase):
    def __init__(self, s):
        self.s = s
        self.i = 0
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b)
        if self.i + n > len(self.s):
            n = len(self.s) - self.i
        b[:n] = self.s[self.i:self.i+n]
        self.i += n
        return n
    def seek(self, pos, whence=0):
        if whence == 0:
            self.i = pos
        elif whence == 1:
            self.i += pos
        else:
            raise ValueError('whence must be 0 or 1')
    def tell(self):
        return self.i
    def writable(self):
        return False
    def write(self, b):
        raise NotImplementedError
    def flush(self):
        pass

f = File(b'abcdefghij')
f.seek(3)
print(f.read(1
